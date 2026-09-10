from pathlib import Path
from typing import Dict, List, Tuple, Union

from dataclasses import dataclass
import cutscene_remover_data as cutscene_remover

from pyisotools.iso import GamecubeISO
import shutil
import yaml

class GameCubeISOProcessor:
    """A processor to extract and reassemble native Nintendo GameCube ISO/GCM file archives."""
    def __init__(self):
        pass

    def extract(self, iso_path: str, extract_to_dir: str) -> None:
        """
        Extracts all system configurations (sys) and game assets (files)
        from a GameCube disc image into a structured local directory.
        """
        # Convert strings to Path objects to prevent internal library attribute errors
        iso_file = Path(iso_path).resolve()
        dest_dir = Path(extract_to_dir).resolve()

        if not iso_file.is_file():
            raise FileNotFoundError(f"Source ISO not found: {iso_file}")

        print(f"Opening GameCube archive: {iso_file}...")
        iso = GamecubeISO.from_iso(iso_file)

        print(f"Extracting filesystem contents to '{dest_dir}'...")
        # Path object satisfies the internal .parent call
        iso.extract(dest_dir)
        print("Extraction completed successfully.")

    def reassemble(self, source_dir: str, output_iso_path: str) -> None:
        """
        Takes an extracted GameCube project folder structure and builds a valid,
        bootable GameCube ISO file from it.
        """
        src_path = Path(source_dir).resolve()
        out_file = Path(output_iso_path).resolve()

        sys_dir = src_path / "sys"
        files_dir = src_path / "files"

        if not sys_dir.is_dir() or not files_dir.is_dir():
            raise ValueError(
                f"Invalid GameCube folder structure in '{src_path}'. "
                "Must contain 'sys' and 'files' subdirectories."
            )

        print(f"Parsing extracted folder layout: {src_path}...")
        iso = GamecubeISO.from_root(src_path, True)

        print(f"Building and packing game image -> {out_file}...")
        iso.build(out_file)
        print("Reassembly complete. File is ready for use.")

#Dataclass for Options, basically a lot o
@dataclass
class FalseboundPatcherOptions:
    Option1: bool = False
    CutsceneRemover: bool = False
    BaseCaptureRewards: bool = False
    ShopsOpen: bool = False
    RandomizeShops: bool = False
    RandomizeBaseGold: bool = False
    MissionClearGold: bool = False
    MissionClearItems: bool = False

class FalseboundPatcher:
    def __init__(self, extracted_root_path: Union[str, Path]):
        """
        Initializes the patching engine.
        :param extracted_root_path: The directory where Dolphin extracted the game
                                    (contains 'sys' and 'files' folders).
        """
        self.root = Path(extracted_root_path)
        if not self.root.exists():
            raise FileNotFoundError(f"Extracted game directory not found at: {self.root}")

    def _apply_patches_to_buffer(self, buffer: bytearray, single_bytes: Dict[int, int],
                                 byte_blocks: List[Tuple[int, bytes]]) -> bool:
        """Processes and validates the byte injections inside the active buffer."""
        # 1. Apply single-byte programmatic overrides
        if single_bytes:
            for offset, value in single_bytes.items():
                if offset >= len(buffer):
                    print(f"[-] Error: Single-byte offset {hex(offset)} is out of file bounds.")
                    return False
                if not (0 <= value <= 255):
                    print(f"[-] Error: Value {value} at offset {hex(offset)} must fit inside 1 byte (0-255).")
                    return False
                buffer[offset] = value

        # 2. Apply arbitrary length byte strings
        if byte_blocks:
            for offset, byte_payload in byte_blocks:
                if not isinstance(byte_payload, (bytes, bytearray)):
                    print(f"[-] Error: Payload at {hex(offset)} must be bytes/bytearray.")
                    return False

                end_offset = offset + len(byte_payload)
                if end_offset > len(buffer):
                    print(f"[-] Error: Byte block at {hex(offset)} overflows file size.")
                    return False

                buffer[offset:end_offset] = byte_payload

        return True

    #Generic File Patcher
    def patch_file(self, internal_path: str, single_bytes: Dict[int, int] = None,
                   byte_blocks: List[Tuple[int, bytes]] = None) -> bool:
        """
        The main public patch function.
        Loads the file, runs the transformations, validates memory, and saves.

        :param internal_path: File location relative to root (e.g., "sys/main.dol", "files/mission.lsc")
        :param single_bytes: Dictionary of {hex_offset: 1_byte_integer_value}
        :param byte_blocks: List of tuples containing [(hex_offset, b'arbitrary_bytes')]
        """
        target_file_path = self.root / internal_path
        if not target_file_path.exists():
            print(f"[-] Skipping: '{internal_path}' does not exist in this workspace.")
            return False

        print(f"[+] Patching file: {internal_path}")

        # Read file directly into an active, mutable buffer
        with open(target_file_path, "rb") as f:
            mutable_buffer = bytearray(f.read())

        # Modify the bytes using our internal helper
        if not self._apply_patches_to_buffer(mutable_buffer, single_bytes, byte_blocks):
            print(f"[-] Patch execution aborted for {internal_path} due to validation errors.")
            return False

        # Write the updated buffer stream back to the storage drive
        with open(target_file_path, "wb") as f:
            f.write(mutable_buffer)

        print(f"[+] Successfully saved changes to: {internal_path}")
        return True

    # Patches Main DOL with arbitrary Patch contents
    def patch_main_dol(self,extract_dir: str, patch: List[Tuple[int, bytes]] = None):
        print (extract_dir)
        internal_path = extract_dir + r"\sys\main.dol"
        self.patch_file(internal_path, byte_blocks=patch)

    # Patches specified LSC files with arbitrary Patch contents
    def patch_lsc_blocks(self,extract_dir :str, lsc_id:str, lsc_patches: List[Tuple[int, bytes]] = None):
        internal_path = rf"{extract_dir}\files\{lsc_id}"
        if lsc_patches:
            self.patch_file(internal_path, byte_blocks=lsc_patches)

    # Patches specified LSC files with arbitrary Patch contents
    def patch_lsc_bytes(self, extract_dir: str, lsc_id: str, lsc_patches: List[Dict[int, int]] = None,):
        internal_path = rf"{extract_dir}\files\{lsc_id}"
        if lsc_patches:
            for patch in lsc_patches:
                self.patch_file(internal_path, single_bytes=patch)


    #Basically coordinates patching everything that needs to be patched
    def patch_all (self, extract_dir: str, lsc_list: List[str], config: FalseboundPatcherOptions):
        print ("WIP")
        ### MAIN/START NOT PRESENT HERE, JUST LSC PATCHES ###
        ### LSC Files ###
        for lsc in lsc_list:
            # Empty Array
            dol_blocks = []
            dol_bytes = []
            # Here's some logic for Various things that live in the LSC files
            if config.CutsceneRemover:
                csr_patch = getattr(cutscene_remover, lsc)
                dol_blocks += csr_patch
            # Things where we have blocks of bytes
            if dol_blocks:
                self.patch_lsc_blocks(extract_dir, f"{lsc}.lsc", dol_blocks)


    def cutscene_remover(self,EXTRACTED_GAME_DIR,lsc_files):
        # Patch the files in the temp directory
        try:
            # Initialize the Falsebound patcher class
            patcher = FalseboundPatcher(EXTRACTED_GAME_DIR)
            # Patches all LSC files "Y01.lsc"
            for file in lsc_files:
                file_patch = getattr(cutscene_remover, file)
                patcher.patch_lsc_blocks(EXTRACTED_GAME_DIR, f"{file}.lsc",file_patch)
                print(f"\n[+] Base Patches to LSC file '{file}' have been saved!")
        except Exception as cutscene_remover_exception:
            print(f"[-] Cutscene Remover patch failed due to runtime error: {cutscene_remover_exception}")

# --- Main programming Loop ---
if __name__ == "__main__":
    # Load Options from the Options.yaml file
    with open("Options.yaml", "r") as yaml_file:
        config = yaml.safe_load(yaml_file)
    ISO_FILE_PATH = config["iso_path"]
    TEMP_EXTRACTED_GAME_DIR = config["temp_path"]
    OUTPUT_ISO_PATH = config["output_path"]
    # Falsebound options class reused from Archipelago to generate a patch file
    options = FalseboundPatcherOptions(CutsceneRemover=True)
    fbk_patch = FalseboundPatcher(TEMP_EXTRACTED_GAME_DIR)
    # Initialize the ISO processor
    gc_processor = GameCubeISOProcessor()
    # Extract file to temporary ISO
    try:
        gc_processor.extract(
            iso_path=ISO_FILE_PATH,
            extract_to_dir=TEMP_EXTRACTED_GAME_DIR
        )
        print("[+] Successfully extracted game ISO.")
    except Exception as e:
        print(f"[-] Problem with extracting game ISO: {e}")
    TEMP_EXTRACTED_GAME_DIR += r"\root"
    TEMP_EXTRACTED_ROOT_DIR = TEMP_EXTRACTED_GAME_DIR + r"\root"
    #Cutscene Remover stuff
    fbk_patch.cutscene_remover(TEMP_EXTRACTED_ROOT_DIR,cutscene_remover.YUGI_FILES)
    fbk_patch.cutscene_remover(TEMP_EXTRACTED_ROOT_DIR,cutscene_remover.KAIBA_FILES)
    fbk_patch.cutscene_remover(TEMP_EXTRACTED_ROOT_DIR,cutscene_remover.JOEY_FILES)
    # Reassemble the ISO
    try:
        gc_processor.reassemble(
            source_dir=TEMP_EXTRACTED_ROOT_DIR,
            output_iso_path=OUTPUT_ISO_PATH
        )
        print("[+] Successfully assembled  game ISO.")
    except Exception as e:
        print(f"[-] Problem with reassembling game ISO: {e}")
    # Clear temp path
    for item in Path(TEMP_EXTRACTED_GAME_DIR).iterdir():
        try:
            if item.is_file() or item.is_symlink():
                item.unlink()  # Deletes files or symbolic links
            elif item.is_dir():
                shutil.rmtree(item)  # Deletes subfolders and their contents
        except Exception as e:
            print(f"Failed to delete {item}. Reason: {e}")
    print ("Cleared Temp files. Happy Playing!")