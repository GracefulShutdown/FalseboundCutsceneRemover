"""
DOES NOT PATCH YOUR ROMS, CHOOSE THE OTHER FILES
This file basically contains a bunch of stuff to remove cutscenes
DOES NOT PATCH YOUR ROMS, CHOOSE THE OTHER FILES
"""

# Main Patch constants
BLANK_DIALOGUE = "0016FFFF030000FF"  #02636F6D6D616E64"
BLANK_CUTSCENE = "000C00"

# Probably missing the ending cutscenes, because those weren't patched files. Easy enough to fix.

YUGI_FILES = [
    "y01","y02","y03","y04","y05",
    "y06","y07","y08","y09","y10",
    "y11","Y12","Y13","Y14","Y15",
    "Y16","Y17","Y18","Y19","Y20",
    "Y21","Y22","Y23",
]
KAIBA_FILES = [
    "S01","S02","S03","S04","S05",
    "S06","S07","S08","S09","S10",
    "S11","S12","S13","S14","S15",
    "S16","S17","S18","S19","S20",
    "S21","S22",
]
JOEY_FILES = [
    "J01","J02","J03","J04","J05",
    "J06","J07","J08","J09","J10",
    "J11",
]


y01 = [
    # Opening cutscene
    (0x290, bytes.fromhex(BLANK_CUTSCENE)),
    # Pre-Mission
    (0x620, bytes.fromhex(BLANK_DIALOGUE)),
    (0x630, bytes.fromhex(BLANK_DIALOGUE)),
    (0x640, bytes.fromhex(BLANK_DIALOGUE)),
    (0x650, bytes.fromhex(BLANK_DIALOGUE)),
    (0x660, bytes.fromhex(BLANK_DIALOGUE)),
    (0x670, bytes.fromhex(BLANK_DIALOGUE)),
    (0x680, bytes.fromhex(BLANK_DIALOGUE)),
    (0x690, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x700, bytes.fromhex(BLANK_DIALOGUE)),
    (0x710, bytes.fromhex(BLANK_DIALOGUE)),
    (0x720, bytes.fromhex(BLANK_DIALOGUE)),
    (0x730, bytes.fromhex(BLANK_DIALOGUE)),
    # Exit Cutscene
    (0x11D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x11E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x11F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1200, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1210, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1220, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1230, bytes.fromhex(BLANK_DIALOGUE)),
    # We Successfully freed RUTHUM!
    (0xae0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xaf0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xb00, bytes.fromhex(BLANK_DIALOGUE)),
    (0xb10, bytes.fromhex(BLANK_DIALOGUE)),
    (0xb20, bytes.fromhex(BLANK_DIALOGUE)),
    # Silver Fang (marshalls)
    (0xea0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xeb0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xec0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xfa0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xfb0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xfc0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x10a0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x10b0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x10c0, bytes.fromhex(BLANK_DIALOGUE)),
    # "It's almost time to face enemy marshalls"
    (0xc70, bytes.fromhex(BLANK_DIALOGUE)),
    (0xc80, bytes.fromhex(BLANK_DIALOGUE)),
    (0xc90, bytes.fromhex(BLANK_DIALOGUE)),
    (0xca0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xcb0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xcc0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xcd0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xce0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xcf0, bytes.fromhex(BLANK_DIALOGUE)),
    # "It's time to attack the Main Base"
    (0xbb0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xbc0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xbd0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xbe0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xbf0, bytes.fromhex(BLANK_DIALOGUE)),
    # Etos lines
    (0x890, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8a0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8b0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8c0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x940, bytes.fromhex(BLANK_DIALOGUE)),
    (0x950, bytes.fromhex(BLANK_DIALOGUE)),
    (0x960, bytes.fromhex(BLANK_DIALOGUE)),
    (0x970, bytes.fromhex(BLANK_DIALOGUE)),
    (0x9F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA00, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA10, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA20, bytes.fromhex(BLANK_DIALOGUE)),
    # Start of game Dialogue
    (0x3F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x400, bytes.fromhex(BLANK_DIALOGUE)),
    (0x410, bytes.fromhex(BLANK_DIALOGUE)),
    (0x420, bytes.fromhex(BLANK_DIALOGUE)),
    (0x430, bytes.fromhex(BLANK_DIALOGUE)),
    (0x440, bytes.fromhex(BLANK_DIALOGUE)),
    (0x450, bytes.fromhex(BLANK_DIALOGUE)),
    (0x460, bytes.fromhex(BLANK_DIALOGUE)),
    (0x470, bytes.fromhex(BLANK_DIALOGUE)),
    (0x480, bytes.fromhex(BLANK_DIALOGUE)),
    (0x490, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4a0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4b0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4c0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4d0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4e0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4f0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x500, bytes.fromhex(BLANK_DIALOGUE)),
    (0x510, bytes.fromhex(BLANK_DIALOGUE)),
    (0x520, bytes.fromhex(BLANK_DIALOGUE)),
    (0x530, bytes.fromhex(BLANK_DIALOGUE)),
    (0x540, bytes.fromhex(BLANK_DIALOGUE)),
    (0x550, bytes.fromhex(BLANK_DIALOGUE)),
    (0x560, bytes.fromhex(BLANK_DIALOGUE)),
    (0x570, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x300, bytes.fromhex(BLANK_DIALOGUE)),
    (0x310, bytes.fromhex(BLANK_DIALOGUE)),
    (0x320, bytes.fromhex(BLANK_DIALOGUE)),
    (0x330, bytes.fromhex(BLANK_DIALOGUE)),
    (0x340, bytes.fromhex(BLANK_DIALOGUE)),
    (0x350, bytes.fromhex(BLANK_DIALOGUE)),
    (0x360, bytes.fromhex(BLANK_DIALOGUE)),
    (0x370, bytes.fromhex(BLANK_DIALOGUE)),
    (0x380, bytes.fromhex(BLANK_DIALOGUE)),
    (0x390, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3a0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3b0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3c0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3d0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3e0, bytes.fromhex(BLANK_DIALOGUE)),

]

y02 = [
    # Pre-mission
    (0x200, bytes.fromhex(BLANK_DIALOGUE)),
    (0x210, bytes.fromhex(BLANK_DIALOGUE)),
    (0x220, bytes.fromhex(BLANK_DIALOGUE)),
    (0x230, bytes.fromhex(BLANK_DIALOGUE)),
    (0x240, bytes.fromhex(BLANK_DIALOGUE)),
    (0x250, bytes.fromhex(BLANK_DIALOGUE)),
    (0x260, bytes.fromhex(BLANK_DIALOGUE)),
    (0x270, bytes.fromhex(BLANK_DIALOGUE)),
    (0x280, bytes.fromhex(BLANK_DIALOGUE)),
    (0x290, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2F0, bytes.fromhex(BLANK_DIALOGUE)),
    # Opening Mission talk about the fort being undefended
    (0x3D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x400, bytes.fromhex(BLANK_DIALOGUE)),
    (0x410, bytes.fromhex(BLANK_DIALOGUE)),
    # "What do you mean by Equipment?"
    (0x5A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x5B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x5C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x5D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x5E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x5F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x600, bytes.fromhex(BLANK_DIALOGUE)),
    (0x610, bytes.fromhex(BLANK_DIALOGUE)),
    (0x620, bytes.fromhex(BLANK_DIALOGUE)),
    # Sebeckal Encounter at enemy Base
    (0x6B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6C0, bytes.fromhex(BLANK_DIALOGUE)),
    # 05C0 - "Encountered Monsters"
    (0x850, bytes.fromhex(BLANK_DIALOGUE)),
    # End of mission Cutscene Sebeckel/Yugi/Tristan
    (0x9F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA00, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA10, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA20, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA30, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA40, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA50, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA60, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA70, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA80, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA90, bytes.fromhex(BLANK_DIALOGUE)),
    (0xAA0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xAB0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xAC0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xAD0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xAE0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xAF0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB00, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB10, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB20, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB30, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB40, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB50, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0xC10, bytes.fromhex(BLANK_DIALOGUE)),
]

y03 = [
    # Base burning event
    (0x5A0, bytes.fromhex(BLANK_CUTSCENE)),
    # Pre-Mission
    (0x1F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x200, bytes.fromhex(BLANK_DIALOGUE)),
    (0x210, bytes.fromhex(BLANK_DIALOGUE)),
    (0x220, bytes.fromhex(BLANK_DIALOGUE)),
    (0x230, bytes.fromhex(BLANK_DIALOGUE)),
    (0x240, bytes.fromhex(BLANK_DIALOGUE)),
    (0x250, bytes.fromhex(BLANK_DIALOGUE)),
    (0x260, bytes.fromhex(BLANK_DIALOGUE)),
    (0x270, bytes.fromhex(BLANK_DIALOGUE)),
    (0x280, bytes.fromhex(BLANK_DIALOGUE)),
    (0x290, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2F0, bytes.fromhex(BLANK_DIALOGUE)),
    # Start of mission cutscene about the base
    (0x3F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x400, bytes.fromhex(BLANK_DIALOGUE)),
    (0x410, bytes.fromhex(BLANK_DIALOGUE)),
    (0x420, bytes.fromhex(BLANK_DIALOGUE)),
    (0x430, bytes.fromhex(BLANK_DIALOGUE)),
    (0x440, bytes.fromhex(BLANK_DIALOGUE)),
    (0x450, bytes.fromhex(BLANK_DIALOGUE)),
    # Granus Dialogue
    (0x6B0, bytes.fromhex(BLANK_DIALOGUE)),
    # Winged Dragon, Guardian of the Fortress #2
    (0x790, bytes.fromhex(BLANK_DIALOGUE)),
    (0x7A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x7B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x7C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x7D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x7E0, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0x910, bytes.fromhex(BLANK_DIALOGUE)),
]

y04 = [
    # Bakura Base disabling event
    (0x700, bytes.fromhex(BLANK_CUTSCENE)),
    # Pre-Mission
    (0x1F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x200, bytes.fromhex(BLANK_DIALOGUE)),
    (0x210, bytes.fromhex(BLANK_DIALOGUE)),
    # Start of mission cutscene about how well defended the base is
    (0x310, bytes.fromhex(BLANK_DIALOGUE)),
    (0x320, bytes.fromhex(BLANK_DIALOGUE)),
    (0x330, bytes.fromhex(BLANK_DIALOGUE)),
    (0x340, bytes.fromhex(BLANK_DIALOGUE)),
    # Bakura Cannon scene: Liberate both advance bases
    (0x500, bytes.fromhex(BLANK_DIALOGUE)),
    (0x510, bytes.fromhex(BLANK_DIALOGUE)),
    (0x520, bytes.fromhex(BLANK_DIALOGUE)),
    (0x530, bytes.fromhex(BLANK_DIALOGUE)),
    (0x540, bytes.fromhex(BLANK_DIALOGUE)),
    (0x550, bytes.fromhex(BLANK_DIALOGUE)),
    (0x560, bytes.fromhex(BLANK_DIALOGUE)),
    (0x570, bytes.fromhex(BLANK_DIALOGUE)),
    (0x580, bytes.fromhex(BLANK_DIALOGUE)),
    (0x590, bytes.fromhex(BLANK_DIALOGUE)),
    (0x5A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x5B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x5C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x5D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x5E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x5F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x600, bytes.fromhex(BLANK_DIALOGUE)),
    (0x610, bytes.fromhex(BLANK_DIALOGUE)),
    # Kepulia Dialogue
    (0x820, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0x8B0, bytes.fromhex(BLANK_DIALOGUE)),
    # End cutscene, Bakura disables the cannons
    (0x9B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x9C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x9D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x9E0, bytes.fromhex(BLANK_DIALOGUE)),
    # Bakura Cannon Scene: You set off a cannon
    (0xA70, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA80, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA90, bytes.fromhex(BLANK_DIALOGUE)),
    (0xAA0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xAB0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xAC0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xAD0, bytes.fromhex(BLANK_DIALOGUE)),
    # End cutscene if you don't wait for Bakura
    (0xB60, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB70, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB80, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB90, bytes.fromhex(BLANK_DIALOGUE)),
]

y05 = [
    # Pre-Mission
    (0x200, bytes.fromhex(BLANK_DIALOGUE)),
    (0x210, bytes.fromhex(BLANK_DIALOGUE)),
    (0x220, bytes.fromhex(BLANK_DIALOGUE)),
    (0x230, bytes.fromhex(BLANK_DIALOGUE)),
    (0x240, bytes.fromhex(BLANK_DIALOGUE)),
    (0x250, bytes.fromhex(BLANK_DIALOGUE)),
    (0x260, bytes.fromhex(BLANK_DIALOGUE)),
    # Secmayton
    (0x4C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4D0, bytes.fromhex(BLANK_DIALOGUE)),
    # Mako-Yugi Scene, Mako joins the party
    (0x5D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x5E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x5F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x600, bytes.fromhex(BLANK_DIALOGUE)),
    (0x610, bytes.fromhex(BLANK_DIALOGUE)),
    # 05C0 - "Encountered Monsters"
    (0x7a0, bytes.fromhex(BLANK_DIALOGUE)),
    # 05C0 - "Encountered Monsters"
    (0x980, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0xa80, bytes.fromhex(BLANK_DIALOGUE)),
    # Ending Mako-Yugi Scene, you finish the enemy off before Mako arrives
    (0xB90, bytes.fromhex(BLANK_DIALOGUE)),
    (0xBA0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xBB0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xBC0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xBD0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xBE0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xBF0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xC00, bytes.fromhex(BLANK_DIALOGUE)),
]

y06 = [
    # Pre-mission
    (0x1C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1F0, bytes.fromhex(BLANK_DIALOGUE)),
    # Yugi-Shimon Beastly Badlands
    (0x310, bytes.fromhex(BLANK_DIALOGUE)),
    (0x320, bytes.fromhex(BLANK_DIALOGUE)),
    (0x330, bytes.fromhex(BLANK_DIALOGUE)),
    (0x340, bytes.fromhex(BLANK_DIALOGUE)),
    (0x350, bytes.fromhex(BLANK_DIALOGUE)),
    (0x360, bytes.fromhex(BLANK_DIALOGUE)),
    # Darkness
    (0x4c0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4d0, bytes.fromhex(BLANK_DIALOGUE)),
    # Illusionary Gentleman encounter Before?
    (0x650, bytes.fromhex(BLANK_DIALOGUE)),
    (0x660, bytes.fromhex(BLANK_DIALOGUE)),
    (0x670, bytes.fromhex(BLANK_DIALOGUE)),
    # Illusionary Gentleman encounter after winning
    (0x6F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x700, bytes.fromhex(BLANK_DIALOGUE)),
    (0x710, bytes.fromhex(BLANK_DIALOGUE)),
    # Summoned Skull encounter
    (0x8e0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8f0, bytes.fromhex(BLANK_DIALOGUE)),
    # Summoned Skull encounter - You Lose
    (0x970, bytes.fromhex(BLANK_DIALOGUE)),
    (0x980, bytes.fromhex(BLANK_DIALOGUE)),
    (0x990, bytes.fromhex(BLANK_DIALOGUE)),
    # Summoned Skull encounter - You win
    (0x9f0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xa00, bytes.fromhex(BLANK_DIALOGUE)),
    (0xa10, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0xae0, bytes.fromhex(BLANK_DIALOGUE)),
    # Darkness post-defeat
    (0xb50, bytes.fromhex(BLANK_DIALOGUE)),
    # Dark Magician joins
    (0xBE0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xBF0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xC00, bytes.fromhex(BLANK_DIALOGUE)),
    (0xC10, bytes.fromhex(BLANK_DIALOGUE)),
    (0xC20, bytes.fromhex(BLANK_DIALOGUE)),
    (0xC30, bytes.fromhex(BLANK_DIALOGUE)),
    (0xC40, bytes.fromhex(BLANK_DIALOGUE)),
    (0xC50, bytes.fromhex(BLANK_DIALOGUE)),
]

y07 = [
    # Haysheen/Scott/The Gang Cutscenes
    (0xD50, bytes.fromhex(BLANK_CUTSCENE)),
    (0xDD0, bytes.fromhex(BLANK_CUTSCENE)),
    # Pre-mission
    (0x240, bytes.fromhex(BLANK_DIALOGUE)),
    (0x250, bytes.fromhex(BLANK_DIALOGUE)),
    (0x260, bytes.fromhex(BLANK_DIALOGUE)),
    (0x270, bytes.fromhex(BLANK_DIALOGUE)),
    (0x280, bytes.fromhex(BLANK_DIALOGUE)),
    (0x290, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Rolecall for everyone
    (0x380, bytes.fromhex(BLANK_DIALOGUE)),
    (0x390, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3E0, bytes.fromhex(BLANK_DIALOGUE)),
    # Gemini Elves reunion
    (0x580, bytes.fromhex(BLANK_DIALOGUE)),
    (0x590, bytes.fromhex(BLANK_DIALOGUE)),
    (0x5A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x5B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x5C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x5D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x5E0, bytes.fromhex(BLANK_DIALOGUE)),
    # Gemini Elves (if you don't have Kachua)
    (0x700, bytes.fromhex(BLANK_DIALOGUE)),
    (0x710, bytes.fromhex(BLANK_DIALOGUE)),
    (0x720, bytes.fromhex(BLANK_DIALOGUE)),
    (0x730, bytes.fromhex(BLANK_DIALOGUE)),
    (0x740, bytes.fromhex(BLANK_DIALOGUE)),
    # Joey Joins overworld
    (0x890, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8E0, bytes.fromhex(BLANK_DIALOGUE)),
    # Mai Joins overworld
    (0xA30, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA40, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA50, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA60, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA70, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA80, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA90, bytes.fromhex(BLANK_DIALOGUE)),
    # Haysheen Encounter "Judge Judy and Executioner"
    (0xb40, bytes.fromhex(BLANK_DIALOGUE)),
    (0xb50, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0xbe0, bytes.fromhex(BLANK_DIALOGUE)),
    # Haysheen retreating
    (0xcd0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xce0, bytes.fromhex(BLANK_DIALOGUE)),
    # Enter Scott (Long, possibly has things skip)
    (0xD80, bytes.fromhex(BLANK_DIALOGUE)),
    (0xD90, bytes.fromhex(BLANK_DIALOGUE)),
    (0xDA0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xDB0, bytes.fromhex(BLANK_DIALOGUE)),
    #(0xDC0, bytes.fromhex(BLANK_DIALOGUE)),
    #(0xDD0, bytes.fromhex(BLANK_DIALOGUE)),
    #(0xDE0, bytes.fromhex(BLANK_DIALOGUE)),
    #(0xDF0, bytes.fromhex(BLANK_DIALOGUE)),
    #(0xE00, bytes.fromhex(BLANK_DIALOGUE)),
    #(0xE10, bytes.fromhex(BLANK_DIALOGUE)),
    #(0xE20, bytes.fromhex(BLANK_DIALOGUE)),
    #(0xE30, bytes.fromhex(BLANK_DIALOGUE)),
    #(0xE40, bytes.fromhex(BLANK_DIALOGUE)),
    #(0xE50, bytes.fromhex(BLANK_DIALOGUE)),
    #(0xE60, bytes.fromhex(BLANK_DIALOGUE)),
    (0xE70, bytes.fromhex(BLANK_DIALOGUE)),
    (0xE80, bytes.fromhex(BLANK_DIALOGUE)),
    (0xE90, bytes.fromhex(BLANK_DIALOGUE)),
    #(0xEA0, bytes.fromhex(BLANK_DIALOGUE)),
    #(0xEB0, bytes.fromhex(BLANK_DIALOGUE)),
    #(0xEC0, bytes.fromhex(BLANK_DIALOGUE)),
    #(0xED0, bytes.fromhex(BLANK_DIALOGUE)),
    #(0xEE0, bytes.fromhex(BLANK_DIALOGUE)),
    #(0xEF0, bytes.fromhex(BLANK_DIALOGUE)),
    #(0xF00, bytes.fromhex(BLANK_DIALOGUE)),
    #(0xF10, bytes.fromhex(BLANK_DIALOGUE)),
    (0xF20, bytes.fromhex(BLANK_DIALOGUE)),
    (0xF30, bytes.fromhex(BLANK_DIALOGUE)),
    (0xF40, bytes.fromhex(BLANK_DIALOGUE)),
    (0xF50, bytes.fromhex(BLANK_DIALOGUE)),
    (0xF60, bytes.fromhex(BLANK_DIALOGUE)),
]

y08 = [
    # Pre-Mission
    (0x200, bytes.fromhex(BLANK_DIALOGUE)),
    (0x210, bytes.fromhex(BLANK_DIALOGUE)),
    (0x220, bytes.fromhex(BLANK_DIALOGUE)),
    (0x230, bytes.fromhex(BLANK_DIALOGUE)),
    (0x240, bytes.fromhex(BLANK_DIALOGUE)),
    (0x250, bytes.fromhex(BLANK_DIALOGUE)),
    # Pre-objective cutscene
    (0x370, bytes.fromhex(BLANK_DIALOGUE)),
    (0x380, bytes.fromhex(BLANK_DIALOGUE)),
    (0x390, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3F0, bytes.fromhex(BLANK_DIALOGUE)),
    # Tea: Time to Fight Back
    (0x580, bytes.fromhex(BLANK_DIALOGUE)),
    # Rare Hunter: Pre-fight
    (0x600, bytes.fromhex(BLANK_DIALOGUE)),
    # Baby Dragon
    (0x6E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x700, bytes.fromhex(BLANK_DIALOGUE)),
    (0x710, bytes.fromhex(BLANK_DIALOGUE)),
    (0x720, bytes.fromhex(BLANK_DIALOGUE)),
    (0x730, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0x800, bytes.fromhex(BLANK_DIALOGUE)),
    # Rare Hunter: Defeated
    (0x8b0, bytes.fromhex(BLANK_DIALOGUE)),
    # Rare Hunter: Running Away
    (0x930, bytes.fromhex(BLANK_DIALOGUE)),
    # Tea: Loses, and you fail mission
    (0x9E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x9F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA00, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA10, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA20, bytes.fromhex(BLANK_DIALOGUE)),
]

y09 = [
    # Pre-Mission
    (0x1C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x200, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission beginning
    (0x2E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x300, bytes.fromhex(BLANK_DIALOGUE)),
    (0x310, bytes.fromhex(BLANK_DIALOGUE)),
    (0x320, bytes.fromhex(BLANK_DIALOGUE)),
    (0x330, bytes.fromhex(BLANK_DIALOGUE)),
    (0x340, bytes.fromhex(BLANK_DIALOGUE)),
    (0x350, bytes.fromhex(BLANK_DIALOGUE)),
    (0x360, bytes.fromhex(BLANK_DIALOGUE)),
    (0x370, bytes.fromhex(BLANK_DIALOGUE)),
    # Atensa Encounter
    (0x490, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4a0, bytes.fromhex(BLANK_DIALOGUE)),
    # 05C0 - "Encountered Monsters"
    (0x610, bytes.fromhex(BLANK_DIALOGUE)),
    # Here is where the absolute insanity of Harpie Lady Ocupete begins:
    # Ocupete: Yugi as marshall
    (0x820, bytes.fromhex(BLANK_DIALOGUE)),
    (0x830, bytes.fromhex(BLANK_DIALOGUE)),
    # Ocupete: Joey as marshall
    (0x8E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8F0, bytes.fromhex(BLANK_DIALOGUE)),
    # Ocupete: Tristan as marshall
    (0x9A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x9B0, bytes.fromhex(BLANK_DIALOGUE)),
    # Ocupete: Tea as marshall
    (0xA60, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA70, bytes.fromhex(BLANK_DIALOGUE)),
    # Ocupete: Mai as marshall
    (0xB20, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB30, bytes.fromhex(BLANK_DIALOGUE)),
    # Ocupete: Shimon as marshall
    (0xBE0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xBF0, bytes.fromhex(BLANK_DIALOGUE)),
    # Ocupete: Fizdis as marshall
    (0xCA0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xCB0, bytes.fromhex(BLANK_DIALOGUE)),
    # Ocupete: Mako as marshall
    (0xD60, bytes.fromhex(BLANK_DIALOGUE)),
    (0xD70, bytes.fromhex(BLANK_DIALOGUE)),
    # Ocupete: Bakura as marshall
    (0xE20, bytes.fromhex(BLANK_DIALOGUE)),
    (0xE30, bytes.fromhex(BLANK_DIALOGUE)),
    # Ocupete: Either common or if you don't have anything
    (0xE70, bytes.fromhex(BLANK_DIALOGUE)),
    (0xE80, bytes.fromhex(BLANK_DIALOGUE)),
    (0xE90, bytes.fromhex(BLANK_DIALOGUE)),
    (0xEA0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xEB0, bytes.fromhex(BLANK_DIALOGUE)),
    # Ocupete: Unlocking with Airo
    (0xF80, bytes.fromhex(BLANK_DIALOGUE)),
    (0xF90, bytes.fromhex(BLANK_DIALOGUE)),
    (0xFA0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xFB0, bytes.fromhex(BLANK_DIALOGUE)),
    # Ocupete: Unlocking with Keraino
    (0x10E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x10F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1100, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1110, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0x1210, bytes.fromhex(BLANK_DIALOGUE)),
]

y10 = [
    # Decoy Scott Cutscene
    (0x770, bytes.fromhex(BLANK_CUTSCENE)),
    # Pre-Mission
    (0x1C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x200, bytes.fromhex(BLANK_DIALOGUE)),
    # Intro Mission
    (0x300, bytes.fromhex(BLANK_DIALOGUE)),
    (0x310, bytes.fromhex(BLANK_DIALOGUE)),
    (0x320, bytes.fromhex(BLANK_DIALOGUE)),
    (0x330, bytes.fromhex(BLANK_DIALOGUE)),
    (0x340, bytes.fromhex(BLANK_DIALOGUE)),
    # Dark Magician Girl
    (0x4F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x500, bytes.fromhex(BLANK_DIALOGUE)),
    (0x510, bytes.fromhex(BLANK_DIALOGUE)),
    (0x520, bytes.fromhex(BLANK_DIALOGUE)),
    (0x530, bytes.fromhex(BLANK_DIALOGUE)),
    (0x540, bytes.fromhex(BLANK_DIALOGUE)),
    (0x550, bytes.fromhex(BLANK_DIALOGUE)),
    (0x560, bytes.fromhex(BLANK_DIALOGUE)),
    (0x570, bytes.fromhex(BLANK_DIALOGUE)),
    (0x580, bytes.fromhex(BLANK_DIALOGUE)),
    (0x590, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0x690, bytes.fromhex(BLANK_DIALOGUE)),
    # End cutscene 1
    (0x700, bytes.fromhex(BLANK_DIALOGUE)),
    (0x710, bytes.fromhex(BLANK_DIALOGUE)),
    (0x720, bytes.fromhex(BLANK_DIALOGUE)),
    # End cutscene 2
    (0x790, bytes.fromhex(BLANK_DIALOGUE)),
    (0x7A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x7B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x7C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x7D0, bytes.fromhex(BLANK_DIALOGUE)),
    # End cutscene 3
    (0x8B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x900, bytes.fromhex(BLANK_DIALOGUE)),
    # End cutscene 4
    (0x9C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x9D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x9E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x9F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA00, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA10, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA20, bytes.fromhex(BLANK_DIALOGUE)),
    # 0C24 Unused?
    #(0xA60, bytes.fromhex(BLANK_DIALOGUE)),
]

y11 = [
    # Tea destroys the world cutscene has lots of candidates
    (0x2F0, bytes.fromhex(BLANK_CUTSCENE)),
    (0x7E0, bytes.fromhex(BLANK_CUTSCENE)),
    (0x8A0, bytes.fromhex(BLANK_CUTSCENE)),
    (0xA20, bytes.fromhex(BLANK_CUTSCENE)),
    (0xAE0, bytes.fromhex(BLANK_CUTSCENE)),
    (0xBA0, bytes.fromhex(BLANK_CUTSCENE)),
    (0x10D0, bytes.fromhex(BLANK_CUTSCENE)),
    # Pre-Mission
    (0x1C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x200, bytes.fromhex(BLANK_DIALOGUE)),
    (0x210, bytes.fromhex(BLANK_DIALOGUE)),
    (0x220, bytes.fromhex(BLANK_DIALOGUE)),
    # Time Wizard
    (0x4F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x500, bytes.fromhex(BLANK_DIALOGUE)),
    (0x510, bytes.fromhex(BLANK_DIALOGUE)),
    (0x520, bytes.fromhex(BLANK_DIALOGUE)),
    # Pre-Bad Ending Cutscene
    (0x610, bytes.fromhex(BLANK_DIALOGUE)),
    # Pre-Tea battle
    (0x690, bytes.fromhex(BLANK_DIALOGUE)),
    # 05 BF line
    (0xE80, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Outro
    (0xF10, bytes.fromhex(BLANK_DIALOGUE)),
    (0xF20, bytes.fromhex(BLANK_DIALOGUE)),
    (0xF30, bytes.fromhex(BLANK_DIALOGUE)),
    (0xF40, bytes.fromhex(BLANK_DIALOGUE)),
    (0xF50, bytes.fromhex(BLANK_DIALOGUE)),
    (0xF60, bytes.fromhex(BLANK_DIALOGUE)),
    # Bad Ending Cutscene
    (0x1070, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1080, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1090, bytes.fromhex(BLANK_DIALOGUE)),
    (0x10A0, bytes.fromhex(BLANK_DIALOGUE)),
]

Y12 = [
    # Kaiba Destroys Cannons Cutscene
    (0x4C0, bytes.fromhex(BLANK_CUTSCENE)),
    (0x4D0, bytes.fromhex(BLANK_CUTSCENE)),
    # Pre-Mission
    (0x1C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x200, bytes.fromhex(BLANK_DIALOGUE)),
    (0x210, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Introduction
    (0x300, bytes.fromhex(BLANK_DIALOGUE)),
    (0x310, bytes.fromhex(BLANK_DIALOGUE)),
    (0x320, bytes.fromhex(BLANK_DIALOGUE)),
    (0x330, bytes.fromhex(BLANK_DIALOGUE)),
    (0x340, bytes.fromhex(BLANK_DIALOGUE)),
    # "It's too well defended!"
    (0x480, bytes.fromhex(BLANK_DIALOGUE)),
    # Pre-Joey fight
    (0x5D0, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0x660, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Outro
    (0x6D0, bytes.fromhex(BLANK_DIALOGUE)),
]

Y13 = [
    # Pre-Mission
    (0x1E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x200, bytes.fromhex(BLANK_DIALOGUE)),
    (0x210, bytes.fromhex(BLANK_DIALOGUE)),
    (0x220, bytes.fromhex(BLANK_DIALOGUE)),
    (0x230, bytes.fromhex(BLANK_DIALOGUE)),
    (0x240, bytes.fromhex(BLANK_DIALOGUE)),
    (0x250, bytes.fromhex(BLANK_DIALOGUE)),
    (0x260, bytes.fromhex(BLANK_DIALOGUE)),
    # "You cannot defeat me I...."
    (0x320, bytes.fromhex(BLANK_DIALOGUE)),
    # Joey Encounter, without Mai
    (0x4C0, bytes.fromhex(BLANK_DIALOGUE)),
    # Joey Encounter, with Mai
    (0x520, bytes.fromhex(BLANK_DIALOGUE)),
    (0x530, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0x660, bytes.fromhex(BLANK_DIALOGUE)),
    # Bad Ending
    (0x6D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x700, bytes.fromhex(BLANK_DIALOGUE)),
    (0x710, bytes.fromhex(BLANK_DIALOGUE)),
    (0x720, bytes.fromhex(BLANK_DIALOGUE)),
    (0x730, bytes.fromhex(BLANK_DIALOGUE)),
    (0x740, bytes.fromhex(BLANK_DIALOGUE)),
    (0x750, bytes.fromhex(BLANK_DIALOGUE)),
    (0x760, bytes.fromhex(BLANK_DIALOGUE)),
    (0x770, bytes.fromhex(BLANK_DIALOGUE)),
    # Good Ending
    (0x7D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x7E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x7F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x800, bytes.fromhex(BLANK_DIALOGUE)),
    (0x810, bytes.fromhex(BLANK_DIALOGUE)),
    (0x820, bytes.fromhex(BLANK_DIALOGUE)),
    (0x830, bytes.fromhex(BLANK_DIALOGUE)),
    (0x840, bytes.fromhex(BLANK_DIALOGUE)),
    (0x850, bytes.fromhex(BLANK_DIALOGUE)),
    (0x860, bytes.fromhex(BLANK_DIALOGUE)),
    (0x870, bytes.fromhex(BLANK_DIALOGUE)),
    (0x880, bytes.fromhex(BLANK_DIALOGUE)),
    (0x890, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8E0, bytes.fromhex(BLANK_DIALOGUE)),
]

Y14 = [
    # Pre-Mission
    (0x1C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x200, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission intro
    (0x2F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x300, bytes.fromhex(BLANK_DIALOGUE)),
    (0x310, bytes.fromhex(BLANK_DIALOGUE)),
    # Strings
    (0x460, bytes.fromhex(BLANK_DIALOGUE)),
    # 05C0 - "Encountered Monsters"
    (0x5f0, bytes.fromhex(BLANK_DIALOGUE)),
    # Post-Mission
    (0x7D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x7E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x7F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x800, bytes.fromhex(BLANK_DIALOGUE)),
    (0x810, bytes.fromhex(BLANK_DIALOGUE)),
    (0x820, bytes.fromhex(BLANK_DIALOGUE)),
    (0x830, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0x8E0, bytes.fromhex(BLANK_DIALOGUE)),
]

Y15 = [
    # MISSING: Bad ending, Jakhud dies
    # Pre-Mission
    (0x1F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x200, bytes.fromhex(BLANK_DIALOGUE)),
    (0x210, bytes.fromhex(BLANK_DIALOGUE)),
    (0x220, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission intro
    (0x2F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x300, bytes.fromhex(BLANK_DIALOGUE)),
    (0x310, bytes.fromhex(BLANK_DIALOGUE)),
    (0x320, bytes.fromhex(BLANK_DIALOGUE)),
    (0x330, bytes.fromhex(BLANK_DIALOGUE)),
    (0x340, bytes.fromhex(BLANK_DIALOGUE)),
    (0x350, bytes.fromhex(BLANK_DIALOGUE)),
    (0x360, bytes.fromhex(BLANK_DIALOGUE)),
    (0x370, bytes.fromhex(BLANK_DIALOGUE)),
    # Bakura encounter
    (0x500, bytes.fromhex(BLANK_DIALOGUE)),
    # Good ending
    (0x5C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x5D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x5E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x5F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x600, bytes.fromhex(BLANK_DIALOGUE)),
    (0x610, bytes.fromhex(BLANK_DIALOGUE)),
    (0x620, bytes.fromhex(BLANK_DIALOGUE)),
    (0x630, bytes.fromhex(BLANK_DIALOGUE)),
    (0x640, bytes.fromhex(BLANK_DIALOGUE)),
    (0x650, bytes.fromhex(BLANK_DIALOGUE)),
    (0x660, bytes.fromhex(BLANK_DIALOGUE)),
    (0x670, bytes.fromhex(BLANK_DIALOGUE)),
    (0x680, bytes.fromhex(BLANK_DIALOGUE)),
    (0x690, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6B0, bytes.fromhex(BLANK_DIALOGUE)),
    # Espa Roba Joins
    (0x710, bytes.fromhex(BLANK_DIALOGUE)),
    (0x720, bytes.fromhex(BLANK_DIALOGUE)),
    (0x730, bytes.fromhex(BLANK_DIALOGUE)),
    (0x740, bytes.fromhex(BLANK_DIALOGUE)),
    (0x750, bytes.fromhex(BLANK_DIALOGUE)),
    (0x760, bytes.fromhex(BLANK_DIALOGUE)),
    (0x770, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0x830, bytes.fromhex(BLANK_DIALOGUE)),
]

Y16 = [
    # Pre-Mission
    (0x1C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x200, bytes.fromhex(BLANK_DIALOGUE)),
    (0x210, bytes.fromhex(BLANK_DIALOGUE)),
    (0x220, bytes.fromhex(BLANK_DIALOGUE)),
    # Arkana Start of Mission
    (0x330, bytes.fromhex(BLANK_DIALOGUE)),
    (0x340, bytes.fromhex(BLANK_DIALOGUE)),
    # Arkana Encounter
    (0x440, bytes.fromhex(BLANK_DIALOGUE)),
    (0x450, bytes.fromhex(BLANK_DIALOGUE)),
    # Defeating Arkana
    (0x4B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4F0, bytes.fromhex(BLANK_DIALOGUE)),
    # Arkana Encounter
    (0x640, bytes.fromhex(BLANK_DIALOGUE)),
    (0x650, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission outro
    (0x6B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6F0, bytes.fromhex(BLANK_DIALOGUE)),
]

Y17 = [
    # Pre-Mission
    (0x1C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x200, bytes.fromhex(BLANK_DIALOGUE)),
    (0x210, bytes.fromhex(BLANK_DIALOGUE)),
    # Labyrinth Tank Discovered
    (0x410, bytes.fromhex(BLANK_DIALOGUE)),
    # Dragon Piper Discovered
    (0x4C0, bytes.fromhex(BLANK_DIALOGUE)),
    # Machine King Discovered
    (0x570, bytes.fromhex(BLANK_DIALOGUE)),
    # Beta the Magnet Warrior Discovered
    (0x620, bytes.fromhex(BLANK_DIALOGUE)),
    # Shadi 4 - "Pay the price"
    (0x6E0, bytes.fromhex(BLANK_DIALOGUE)),
    # Shadi 3 - "Test the power"
    (0x760, bytes.fromhex(BLANK_DIALOGUE)),
    # Shadi 2 - "Disturbance in heart"
    (0x7E0, bytes.fromhex(BLANK_DIALOGUE)),
    # Shadi 1 - "Final Task"
    (0x860, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0x9A0, bytes.fromhex(BLANK_DIALOGUE)),
]

Y18 = [
    # Face-Off Cutscene
    (0x2D0, bytes.fromhex(BLANK_CUTSCENE)),
    # Pre-mission
    (0x1C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x200, bytes.fromhex(BLANK_DIALOGUE)),
    (0x210, bytes.fromhex(BLANK_DIALOGUE)),
    # Gaia the Fierce Knight
    (0x4E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x500, bytes.fromhex(BLANK_DIALOGUE)),
    # Gaia the Fierce Knight Encounter
    (0x4E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x500, bytes.fromhex(BLANK_DIALOGUE)),
    # Gaia the Fierce Knight Win
    (0x570, bytes.fromhex(BLANK_DIALOGUE)),
    (0x580, bytes.fromhex(BLANK_DIALOGUE)),
    # Kaiba Fight
    (0x640, bytes.fromhex(BLANK_DIALOGUE)),
    (0x650, bytes.fromhex(BLANK_DIALOGUE)),
    (0x660, bytes.fromhex(BLANK_DIALOGUE)),
    (0x670, bytes.fromhex(BLANK_DIALOGUE)),
    (0x680, bytes.fromhex(BLANK_DIALOGUE)),
    (0x690, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6A0, bytes.fromhex(BLANK_DIALOGUE)),
    # After beating Kaiba
    (0x700, bytes.fromhex(BLANK_DIALOGUE)),
    (0x710, bytes.fromhex(BLANK_DIALOGUE)),
    (0x720, bytes.fromhex(BLANK_DIALOGUE)),
    (0x730, bytes.fromhex(BLANK_DIALOGUE)),
    (0x740, bytes.fromhex(BLANK_DIALOGUE)),
    (0x750, bytes.fromhex(BLANK_DIALOGUE)),
    (0x760, bytes.fromhex(BLANK_DIALOGUE)),
    (0x770, bytes.fromhex(BLANK_DIALOGUE)),
    (0x780, bytes.fromhex(BLANK_DIALOGUE)),
    (0x790, bytes.fromhex(BLANK_DIALOGUE)),
    (0x7A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x7B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x7C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x7D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x7E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x7F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x800, bytes.fromhex(BLANK_DIALOGUE)),
    (0x810, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0x8C0, bytes.fromhex(BLANK_DIALOGUE)),
]

Y19 = [
    # Pre-mission
    (0x1C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1E0, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Intro
    (0x2E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x300, bytes.fromhex(BLANK_DIALOGUE)),
    (0x310, bytes.fromhex(BLANK_DIALOGUE)),
    (0x320, bytes.fromhex(BLANK_DIALOGUE)),
    (0x330, bytes.fromhex(BLANK_DIALOGUE)),
    (0x340, bytes.fromhex(BLANK_DIALOGUE)),
    (0x350, bytes.fromhex(BLANK_DIALOGUE)),
    (0x360, bytes.fromhex(BLANK_DIALOGUE)),
    (0x370, bytes.fromhex(BLANK_DIALOGUE)),
    (0x380, bytes.fromhex(BLANK_DIALOGUE)),
    (0x390, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x400, bytes.fromhex(BLANK_DIALOGUE)),
    (0x410, bytes.fromhex(BLANK_DIALOGUE)),
    (0x420, bytes.fromhex(BLANK_DIALOGUE)),
    (0x430, bytes.fromhex(BLANK_DIALOGUE)),
    (0x440, bytes.fromhex(BLANK_DIALOGUE)),
    # Scott Encounter
    (0x560, bytes.fromhex(BLANK_DIALOGUE)),
    # Harpie Lady Keraino
    (0x630, bytes.fromhex(BLANK_DIALOGUE)),
    (0x640, bytes.fromhex(BLANK_DIALOGUE)),
    (0x650, bytes.fromhex(BLANK_DIALOGUE)),
    (0x660, bytes.fromhex(BLANK_DIALOGUE)),
    (0x670, bytes.fromhex(BLANK_DIALOGUE)),
    # Outro
    (0x730, bytes.fromhex(BLANK_DIALOGUE)),
    (0x740, bytes.fromhex(BLANK_DIALOGUE)),
    (0x750, bytes.fromhex(BLANK_DIALOGUE)),
    (0x760, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0x8C0, bytes.fromhex(BLANK_DIALOGUE)),
]

Y20 = [
    # Mokuba Cutscene
    (0x420, bytes.fromhex(BLANK_CUTSCENE)),
    # Pre-mission
    (0x1C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1E0, bytes.fromhex(BLANK_DIALOGUE)),
    # Odion
    (0x3A0, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0x4A0, bytes.fromhex(BLANK_DIALOGUE)),
]

Y21 = [
    # Scott Cutscene
    (0x350, bytes.fromhex(BLANK_CUTSCENE)),
    # Pre-mission
    (0x1C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1D0, bytes.fromhex(BLANK_DIALOGUE)),
    # Yugi/Joey
    (0x300, bytes.fromhex(BLANK_DIALOGUE)),
    (0x310, bytes.fromhex(BLANK_DIALOGUE)),
    # Alpha the Magnet Warrior
    (0x4A0, bytes.fromhex(BLANK_DIALOGUE)),
    # Outro
    (0x540, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0x5F0, bytes.fromhex(BLANK_DIALOGUE)),
]

Y22 = [
    # Bunch of cutscenes
    (0x780, bytes.fromhex(BLANK_CUTSCENE)),
    (0x790, bytes.fromhex(BLANK_CUTSCENE)),
    (0xA30, bytes.fromhex(BLANK_CUTSCENE)),
    (0xF70, bytes.fromhex(BLANK_CUTSCENE)),
    (0x1000, bytes.fromhex(BLANK_CUTSCENE)),
    (0x10A0, bytes.fromhex(BLANK_CUTSCENE)),
    # Pre-Mission
    (0x1D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1F0, bytes.fromhex(BLANK_DIALOGUE)),
    # Scott
    (0x670, bytes.fromhex(BLANK_DIALOGUE)),
    (0x680, bytes.fromhex(BLANK_DIALOGUE)),
    (0x690, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6D0, bytes.fromhex(BLANK_DIALOGUE)),
    # "What a waste"
    (0x740, bytes.fromhex(BLANK_DIALOGUE)),
    # First encounter with Scott
    (0xA00, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA10, bytes.fromhex(BLANK_DIALOGUE)),
    # Stopped the North Bridge
    (0xB30, bytes.fromhex(BLANK_DIALOGUE)),
    # "We've stopped it from recovering as fast"
    (0xBB0, bytes.fromhex(BLANK_DIALOGUE)),
    # Stopped the South Bridge
    (0xC60, bytes.fromhex(BLANK_DIALOGUE)),
    # "Make it weaker"
    (0xCE0, bytes.fromhex(BLANK_DIALOGUE)),
    # It's too powerful!
    (0xE10, bytes.fromhex(BLANK_DIALOGUE)),
    (0xE20, bytes.fromhex(BLANK_DIALOGUE)),
    (0xE30, bytes.fromhex(BLANK_DIALOGUE)),
    (0xE40, bytes.fromhex(BLANK_DIALOGUE)),
    (0xE50, bytes.fromhex(BLANK_DIALOGUE)),
    # Defeated by Nitemare (I think?)
    (0x1150, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1160, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1170, bytes.fromhex(BLANK_DIALOGUE)),
    # Lose to Scott
    (0x11D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x11E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x11F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1200, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1210, bytes.fromhex(BLANK_DIALOGUE)),
    # Lose to DarkNite
    (0x1270, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1280, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1290, bytes.fromhex(BLANK_DIALOGUE)),
]

Y23 = [
    # Story Ending Cutscene
    (0x1A0, bytes.fromhex(BLANK_CUTSCENE)),
]

S01 = [
    # Opening Cutscene
    (0x290, bytes.fromhex(BLANK_CUTSCENE)),
    # Opening banter between Kaiba and Marthis
    (0x2D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x300, bytes.fromhex(BLANK_DIALOGUE)),
    (0x310, bytes.fromhex(BLANK_DIALOGUE)),
    (0x320, bytes.fromhex(BLANK_DIALOGUE)),
    (0x330, bytes.fromhex(BLANK_DIALOGUE)),
    (0x340, bytes.fromhex(BLANK_DIALOGUE)),
    (0x350, bytes.fromhex(BLANK_DIALOGUE)),
    (0x360, bytes.fromhex(BLANK_DIALOGUE)),
    (0x370, bytes.fromhex(BLANK_DIALOGUE)),
    (0x380, bytes.fromhex(BLANK_DIALOGUE)),
    (0x390, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3C0, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Intro
    (0x470, bytes.fromhex(BLANK_DIALOGUE)),
    (0x480, bytes.fromhex(BLANK_DIALOGUE)),
    (0x490, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x500, bytes.fromhex(BLANK_DIALOGUE)),
    (0x510, bytes.fromhex(BLANK_DIALOGUE)),
    (0x520, bytes.fromhex(BLANK_DIALOGUE)),
    (0x530, bytes.fromhex(BLANK_DIALOGUE)),
    (0x540, bytes.fromhex(BLANK_DIALOGUE)),
    (0x550, bytes.fromhex(BLANK_DIALOGUE)),
    (0x560, bytes.fromhex(BLANK_DIALOGUE)),
    (0x570, bytes.fromhex(BLANK_DIALOGUE)),
    (0x580, bytes.fromhex(BLANK_DIALOGUE)),
    # Malairuka "I fight for the people"
    (0x6F0, bytes.fromhex(BLANK_DIALOGUE)),
    # Jusell "Curse you imperial..."
    (0x770, bytes.fromhex(BLANK_DIALOGUE)),
    # Marthis - Base Capturing the southern base
    (0x820, bytes.fromhex(BLANK_DIALOGUE)),
    (0x830, bytes.fromhex(BLANK_DIALOGUE)),
    (0x840, bytes.fromhex(BLANK_DIALOGUE)),
    (0x850, bytes.fromhex(BLANK_DIALOGUE)),
    # Marthis - Attacking the main base
    (0x8E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x900, bytes.fromhex(BLANK_DIALOGUE)),
    (0x910, bytes.fromhex(BLANK_DIALOGUE)),
    (0x920, bytes.fromhex(BLANK_DIALOGUE)),
    # Marthis - Attacking a Marshall
    (0x9A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x9B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x9C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x9D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x9E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x9F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA00, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA10, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA20, bytes.fromhex(BLANK_DIALOGUE)),
    # 05C0 - "Encountered Monsters"
    (0xB90, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Outro
    (0xC90, bytes.fromhex(BLANK_DIALOGUE)),
    (0xCA0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xCB0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xCC0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xCD0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xCE0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xCF0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xD00, bytes.fromhex(BLANK_DIALOGUE)),
    (0xD10, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0xE20, bytes.fromhex(BLANK_DIALOGUE)),
]

S02 = [
    # Pre-Mission (it's a lot it seems)
    (0x220, bytes.fromhex(BLANK_DIALOGUE)),
    (0x230, bytes.fromhex(BLANK_DIALOGUE)),
    (0x240, bytes.fromhex(BLANK_DIALOGUE)),
    (0x250, bytes.fromhex(BLANK_DIALOGUE)),
    (0x260, bytes.fromhex(BLANK_DIALOGUE)),
    (0x270, bytes.fromhex(BLANK_DIALOGUE)),
    (0x280, bytes.fromhex(BLANK_DIALOGUE)),
    (0x290, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x300, bytes.fromhex(BLANK_DIALOGUE)),
    (0x310, bytes.fromhex(BLANK_DIALOGUE)),
    (0x320, bytes.fromhex(BLANK_DIALOGUE)),
    (0x330, bytes.fromhex(BLANK_DIALOGUE)),
    (0x340, bytes.fromhex(BLANK_DIALOGUE)),
    (0x350, bytes.fromhex(BLANK_DIALOGUE)),
    (0x360, bytes.fromhex(BLANK_DIALOGUE)),
    (0x370, bytes.fromhex(BLANK_DIALOGUE)),
    (0x380, bytes.fromhex(BLANK_DIALOGUE)),
    (0x390, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3E0, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Intro (Keith and Bonz)
    (0x490, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4D0, bytes.fromhex(BLANK_DIALOGUE)),
    # Keith Encounter
    (0x600, bytes.fromhex(BLANK_DIALOGUE)),
    # Bonz Encounter
    (0x680, bytes.fromhex(BLANK_DIALOGUE)),
    # Equipment Tutorial
    (0x700, bytes.fromhex(BLANK_DIALOGUE)),
    (0x710, bytes.fromhex(BLANK_DIALOGUE)),
    (0x720, bytes.fromhex(BLANK_DIALOGUE)),
    (0x730, bytes.fromhex(BLANK_DIALOGUE)),
    (0x740, bytes.fromhex(BLANK_DIALOGUE)),
    (0x750, bytes.fromhex(BLANK_DIALOGUE)),
    (0x760, bytes.fromhex(BLANK_DIALOGUE)),
    (0x770, bytes.fromhex(BLANK_DIALOGUE)),
    (0x780, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Outro
    (0x7F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x800, bytes.fromhex(BLANK_DIALOGUE)),
    (0x810, bytes.fromhex(BLANK_DIALOGUE)),
    (0x820, bytes.fromhex(BLANK_DIALOGUE)),
    (0x830, bytes.fromhex(BLANK_DIALOGUE)),
    (0x840, bytes.fromhex(BLANK_DIALOGUE)),
    (0x850, bytes.fromhex(BLANK_DIALOGUE)),
    (0x860, bytes.fromhex(BLANK_DIALOGUE)),
    (0x870, bytes.fromhex(BLANK_DIALOGUE)),
    (0x880, bytes.fromhex(BLANK_DIALOGUE)),
    (0x890, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x900, bytes.fromhex(BLANK_DIALOGUE)),
    (0x910, bytes.fromhex(BLANK_DIALOGUE)),
    (0x920, bytes.fromhex(BLANK_DIALOGUE)),
    (0x930, bytes.fromhex(BLANK_DIALOGUE)),
    (0x940, bytes.fromhex(BLANK_DIALOGUE)),
    (0x950, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0xA10, bytes.fromhex(BLANK_DIALOGUE)),
]

S03 = [
    # Pegasus intro cutscene
    (0x670, bytes.fromhex(BLANK_CUTSCENE)),
    # Pre-Mission
    (0x1F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x200, bytes.fromhex(BLANK_DIALOGUE)),
    (0x210, bytes.fromhex(BLANK_DIALOGUE)),
    (0x220, bytes.fromhex(BLANK_DIALOGUE)),
    (0x230, bytes.fromhex(BLANK_DIALOGUE)),
    (0x240, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Intro
    (0x380, bytes.fromhex(BLANK_DIALOGUE)),
    (0x390, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x400, bytes.fromhex(BLANK_DIALOGUE)),
    (0x410, bytes.fromhex(BLANK_DIALOGUE)),
    (0x420, bytes.fromhex(BLANK_DIALOGUE)),
    (0x430, bytes.fromhex(BLANK_DIALOGUE)),
    (0x440, bytes.fromhex(BLANK_DIALOGUE)),
    (0x450, bytes.fromhex(BLANK_DIALOGUE)),
    (0x460, bytes.fromhex(BLANK_DIALOGUE)),
    (0x470, bytes.fromhex(BLANK_DIALOGUE)),
    (0x480, bytes.fromhex(BLANK_DIALOGUE)),
    (0x490, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4C0, bytes.fromhex(BLANK_DIALOGUE)),
    # Pegasus Encounter
    (0x5D0, bytes.fromhex(BLANK_DIALOGUE)),
    # Outro - Pegasus part (cutscene is separate)
    (0x630, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0x6F0, bytes.fromhex(BLANK_DIALOGUE)),
]

S04 = [
    # Bunch of cutscenes
    (0x200, bytes.fromhex(BLANK_CUTSCENE)),
    # Possible Music artifacting here
    # Pre-Mission
    (0x270, bytes.fromhex(BLANK_DIALOGUE)),
    (0x280, bytes.fromhex(BLANK_DIALOGUE)),
    (0x290, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x300, bytes.fromhex(BLANK_DIALOGUE)),
    (0x310, bytes.fromhex(BLANK_DIALOGUE)),
    (0x320, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission intro
    (0x410, bytes.fromhex(BLANK_DIALOGUE)),
    (0x420, bytes.fromhex(BLANK_DIALOGUE)),
    (0x430, bytes.fromhex(BLANK_DIALOGUE)),
    (0x440, bytes.fromhex(BLANK_DIALOGUE)),
    (0x450, bytes.fromhex(BLANK_DIALOGUE)),
    (0x460, bytes.fromhex(BLANK_DIALOGUE)),
    (0x470, bytes.fromhex(BLANK_DIALOGUE)),
    (0x480, bytes.fromhex(BLANK_DIALOGUE)),
    (0x490, bytes.fromhex(BLANK_DIALOGUE)),
    # Gamma the Magnet Warrior
    (0x590, bytes.fromhex(BLANK_DIALOGUE)),
    # Marthis Encounter
    (0x650, bytes.fromhex(BLANK_DIALOGUE)),
    # Pegasus Arrives before you clear the mission
    (0x790, bytes.fromhex(BLANK_DIALOGUE)),
    (0x7A0, bytes.fromhex(BLANK_DIALOGUE)),
    # Marthis Dies
    (0x840, bytes.fromhex(BLANK_DIALOGUE)),
    # Lengthy Pegasus cutscene
    (0x880, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x900, bytes.fromhex(BLANK_DIALOGUE)),
    (0x910, bytes.fromhex(BLANK_DIALOGUE)),
    (0x920, bytes.fromhex(BLANK_DIALOGUE)),
    (0x930, bytes.fromhex(BLANK_DIALOGUE)),
    (0x940, bytes.fromhex(BLANK_DIALOGUE)),
    (0x950, bytes.fromhex(BLANK_DIALOGUE)),
    (0x960, bytes.fromhex(BLANK_DIALOGUE)),
    (0x970, bytes.fromhex(BLANK_DIALOGUE)),
    (0x980, bytes.fromhex(BLANK_DIALOGUE)),
    (0x990, bytes.fromhex(BLANK_DIALOGUE)),
    (0x9A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x9B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x9C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x9D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x9E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x9F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA00, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA10, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA20, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA30, bytes.fromhex(BLANK_DIALOGUE)),
    # Lengthy Pegasus Cutscene if you win quickly
    (0xAD0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xAE0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xAF0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB00, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB10, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB20, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB30, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB40, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB50, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB60, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB70, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB80, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB90, bytes.fromhex(BLANK_DIALOGUE)),
    (0xBA0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xBB0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xBC0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xBD0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xBE0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xBF0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xC00, bytes.fromhex(BLANK_DIALOGUE)),
    (0xC10, bytes.fromhex(BLANK_DIALOGUE)),
    (0xC20, bytes.fromhex(BLANK_DIALOGUE)),
    (0xC30, bytes.fromhex(BLANK_DIALOGUE)),
    (0xC40, bytes.fromhex(BLANK_DIALOGUE)),
    (0xC50, bytes.fromhex(BLANK_DIALOGUE)),
    (0xC60, bytes.fromhex(BLANK_DIALOGUE)),
    (0xC70, bytes.fromhex(BLANK_DIALOGUE)),
    (0xC80, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0xD30, bytes.fromhex(BLANK_DIALOGUE)),
]

S05 = [
    # Pre-Mission
    (0x1F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x200, bytes.fromhex(BLANK_DIALOGUE)),
    (0x210, bytes.fromhex(BLANK_DIALOGUE)),
    (0x220, bytes.fromhex(BLANK_DIALOGUE)),
    (0x230, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Intro
    (0x320, bytes.fromhex(BLANK_DIALOGUE)),
    (0x330, bytes.fromhex(BLANK_DIALOGUE)),
    (0x340, bytes.fromhex(BLANK_DIALOGUE)),
    (0x350, bytes.fromhex(BLANK_DIALOGUE)),
    (0x360, bytes.fromhex(BLANK_DIALOGUE)),
    # Pegasus Cutscene (Funny enough, they programmed this in)
    (0x470, bytes.fromhex(BLANK_DIALOGUE)),
    (0x480, bytes.fromhex(BLANK_DIALOGUE)),
    (0x490, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4A0, bytes.fromhex(BLANK_DIALOGUE)),
    # Weevil Encounter
    (0x520, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Outro
    (0x580, bytes.fromhex(BLANK_DIALOGUE)),
    (0x590, bytes.fromhex(BLANK_DIALOGUE)),
    (0x5A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x5B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x5C0, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0x680, bytes.fromhex(BLANK_DIALOGUE)),
]

S06 = [
    # Pre-Mission
    (0x1F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x200, bytes.fromhex(BLANK_DIALOGUE)),
    (0x210, bytes.fromhex(BLANK_DIALOGUE)),
    (0x220, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Intro
    (0x320, bytes.fromhex(BLANK_DIALOGUE)),
    (0x330, bytes.fromhex(BLANK_DIALOGUE)),
    (0x340, bytes.fromhex(BLANK_DIALOGUE)),
    (0x350, bytes.fromhex(BLANK_DIALOGUE)),
    (0x360, bytes.fromhex(BLANK_DIALOGUE)),
    (0x370, bytes.fromhex(BLANK_DIALOGUE)),
    (0x380, bytes.fromhex(BLANK_DIALOGUE)),
    # Rex Raptor Encounter
    (0x490, bytes.fromhex(BLANK_DIALOGUE)),
    # Tiger Axe Encounter
    (0x5F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x600, bytes.fromhex(BLANK_DIALOGUE)),
    # Tiger Axe Recruitment
    (0x670, bytes.fromhex(BLANK_DIALOGUE)),
    (0x680, bytes.fromhex(BLANK_DIALOGUE)),
    (0x690, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Outro
    (0x730, bytes.fromhex(BLANK_DIALOGUE)),
    (0x740, bytes.fromhex(BLANK_DIALOGUE)),
    (0x750, bytes.fromhex(BLANK_DIALOGUE)),
    (0x760, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0x820, bytes.fromhex(BLANK_DIALOGUE)),
]

S07 = [
    #Pre-Mission
    (0x1C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x200, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Intro
    (0x2D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x300, bytes.fromhex(BLANK_DIALOGUE)),
    (0x310, bytes.fromhex(BLANK_DIALOGUE)),
    # Nephel Encounter
    (0x450, bytes.fromhex(BLANK_DIALOGUE)),
    # Garoozis Encounter
    (0x5D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x5E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x5F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x600, bytes.fromhex(BLANK_DIALOGUE)),
    # Moisture Creature Encounter
    (0x910, bytes.fromhex(BLANK_DIALOGUE)),
    (0x920, bytes.fromhex(BLANK_DIALOGUE)),
    (0x930, bytes.fromhex(BLANK_DIALOGUE)),
    (0x940, bytes.fromhex(BLANK_DIALOGUE)),
    (0x950, bytes.fromhex(BLANK_DIALOGUE)),
    (0x960, bytes.fromhex(BLANK_DIALOGUE)),
    (0x970, bytes.fromhex(BLANK_DIALOGUE)),
    (0x980, bytes.fromhex(BLANK_DIALOGUE)),
    (0x990, bytes.fromhex(BLANK_DIALOGUE)),
    (0x9A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x9B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x9C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x9D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x9E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x9F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA00, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA10, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA20, bytes.fromhex(BLANK_DIALOGUE)),
    # Lose the mission dialogue
    (0xB80, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB90, bytes.fromhex(BLANK_DIALOGUE)),
    # Additional Dialogue, Appears to be "We're too late x2"
    (0xC30, bytes.fromhex(BLANK_DIALOGUE)),
    (0xC40, bytes.fromhex(BLANK_DIALOGUE)),
]

S08 = [
    # Pre-Mission
    (0x1C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1F0, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Intro
    (0x2E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x300, bytes.fromhex(BLANK_DIALOGUE)),
    (0x310, bytes.fromhex(BLANK_DIALOGUE)),
    # Sebeckal/Necubetos Encounter
    (0x480, bytes.fromhex(BLANK_DIALOGUE)),
    # Sebeckal/Necubetos Encounter
    (0x500, bytes.fromhex(BLANK_DIALOGUE)),
    # 05C0 - "Encountered Monsters"
    (0x690, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0x8A0, bytes.fromhex(BLANK_DIALOGUE)),
    # Lose the mission text
    (0x940, bytes.fromhex(BLANK_DIALOGUE)),
    (0x950, bytes.fromhex(BLANK_DIALOGUE)),
]

S09 = [
    # Scott Cutscenes
    (0x530, bytes.fromhex(BLANK_CUTSCENE)),
    (0x5C0, bytes.fromhex(BLANK_CUTSCENE)),
    # Pre-Mission
    (0x1C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1F0, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Intro
    (0x300, bytes.fromhex(BLANK_DIALOGUE)),
    (0x310, bytes.fromhex(BLANK_DIALOGUE)),
    (0x320, bytes.fromhex(BLANK_DIALOGUE)),
    (0x330, bytes.fromhex(BLANK_DIALOGUE)),
    (0x340, bytes.fromhex(BLANK_DIALOGUE)),
    (0x350, bytes.fromhex(BLANK_DIALOGUE)),
    # Haysheen Encounter
    (0x470, bytes.fromhex(BLANK_DIALOGUE)),
    (0x480, bytes.fromhex(BLANK_DIALOGUE)),
    # Defeating Haysheen
    (0x4E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4F0, bytes.fromhex(BLANK_DIALOGUE)),
    # Scott Appears
    (0x560, bytes.fromhex(BLANK_DIALOGUE)),
    (0x570, bytes.fromhex(BLANK_DIALOGUE)),
    (0x580, bytes.fromhex(BLANK_DIALOGUE)),
    (0x590, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF
    (0x630, bytes.fromhex(BLANK_DIALOGUE)),
]

S10 = [
    # Mokuba Kidnapping
    (0x980, bytes.fromhex(BLANK_CUTSCENE)),
    # Pre-Mission
    (0x1C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1E0, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Intro
    (0x2E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x300, bytes.fromhex(BLANK_DIALOGUE)),
    (0x310, bytes.fromhex(BLANK_DIALOGUE)),
    (0x320, bytes.fromhex(BLANK_DIALOGUE)),
    # Rare Hunter Encounter
    (0x430, bytes.fromhex(BLANK_DIALOGUE)),
    # Yugi Shows up
    (0x510, bytes.fromhex(BLANK_DIALOGUE)),
    (0x520, bytes.fromhex(BLANK_DIALOGUE)),
    (0x530, bytes.fromhex(BLANK_DIALOGUE)),
    (0x540, bytes.fromhex(BLANK_DIALOGUE)),
    (0x550, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Outro (Rare Hunter)
    (0x730, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Outro (Splitting up)
    (0x780, bytes.fromhex(BLANK_DIALOGUE)),
    (0x790, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0x860, bytes.fromhex(BLANK_DIALOGUE)),
    # Yugi Shows up, defeating Rare Hunter early.
    (0x900, bytes.fromhex(BLANK_DIALOGUE)),
    (0x910, bytes.fromhex(BLANK_DIALOGUE)),
    (0x920, bytes.fromhex(BLANK_DIALOGUE)),
    (0x930, bytes.fromhex(BLANK_DIALOGUE)),
    (0x940, bytes.fromhex(BLANK_DIALOGUE)),
]

S11 = [
    # Decoy Scott Cutscene
    (0x570, bytes.fromhex(BLANK_CUTSCENE)),
    # Pre-Mission
    (0x1C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x200, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Intro
    (0x300, bytes.fromhex(BLANK_DIALOGUE)),
    (0x310, bytes.fromhex(BLANK_DIALOGUE)),
    (0x320, bytes.fromhex(BLANK_DIALOGUE)),
    (0x330, bytes.fromhex(BLANK_DIALOGUE)),
    # "Scott" Encounter
    (0x440, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Outro
    (0x520, bytes.fromhex(BLANK_DIALOGUE)),
    (0x530, bytes.fromhex(BLANK_DIALOGUE)),
    (0x540, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0x630, bytes.fromhex(BLANK_DIALOGUE)),
]

S12 = [
    # Pre-Mission
    (0x1D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x200, bytes.fromhex(BLANK_DIALOGUE)),
    # Pre-Mission (second part)
    (0x240, bytes.fromhex(BLANK_DIALOGUE)),
    (0x250, bytes.fromhex(BLANK_DIALOGUE)),
    (0x260, bytes.fromhex(BLANK_DIALOGUE)),
    (0x270, bytes.fromhex(BLANK_DIALOGUE)),
    (0x280, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Intro
    (0x340, bytes.fromhex(BLANK_DIALOGUE)),
    (0x350, bytes.fromhex(BLANK_DIALOGUE)),
    (0x360, bytes.fromhex(BLANK_DIALOGUE)),
    # Lava Battleguard
    (0x610, bytes.fromhex(BLANK_DIALOGUE)),
    (0x620, bytes.fromhex(BLANK_DIALOGUE)),
    (0x630, bytes.fromhex(BLANK_DIALOGUE)),
    (0x640, bytes.fromhex(BLANK_DIALOGUE)),
    (0x650, bytes.fromhex(BLANK_DIALOGUE)),
    (0x660, bytes.fromhex(BLANK_DIALOGUE)),
    (0x670, bytes.fromhex(BLANK_DIALOGUE)),
    # Lose the mission
    (0x7F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x800, bytes.fromhex(BLANK_DIALOGUE)),
    (0x810, bytes.fromhex(BLANK_DIALOGUE)),
]

S13 = [
    # Pre-Mission
    (0x1C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1F0, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Intro
    (0x2C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x300, bytes.fromhex(BLANK_DIALOGUE)),
    # Encounter Keith
    (0x460, bytes.fromhex(BLANK_DIALOGUE)),
    # 05C0 - "Encountered Monsters"
    (0x5D0, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Outro
    (0x820, bytes.fromhex(BLANK_DIALOGUE)),
    (0x830, bytes.fromhex(BLANK_DIALOGUE)),
    (0x840, bytes.fromhex(BLANK_DIALOGUE)),
    (0x850, bytes.fromhex(BLANK_DIALOGUE)),
    (0x860, bytes.fromhex(BLANK_DIALOGUE)),
    (0x870, bytes.fromhex(BLANK_DIALOGUE)),
    (0x880, bytes.fromhex(BLANK_DIALOGUE)),
    (0x890, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8F0, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0xAF0, bytes.fromhex(BLANK_DIALOGUE)),
]

S14 = [
    # Pre-Mission
    (0x1C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x200, bytes.fromhex(BLANK_DIALOGUE)),
    (0x210, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Intro
    (0x300, bytes.fromhex(BLANK_DIALOGUE)),
    (0x310, bytes.fromhex(BLANK_DIALOGUE)),
    (0x320, bytes.fromhex(BLANK_DIALOGUE)),
    (0x330, bytes.fromhex(BLANK_DIALOGUE)),
    (0x340, bytes.fromhex(BLANK_DIALOGUE)),
    (0x350, bytes.fromhex(BLANK_DIALOGUE)),
    # Buster Blader Encounter
    (0x540, bytes.fromhex(BLANK_DIALOGUE)),
    (0x550, bytes.fromhex(BLANK_DIALOGUE)),
    (0x560, bytes.fromhex(BLANK_DIALOGUE)),
    # Winning the Buster Blader Battle
    (0x5D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x5E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x5F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x600, bytes.fromhex(BLANK_DIALOGUE)),
    (0x610, bytes.fromhex(BLANK_DIALOGUE)),
    # Losing the Buster Blader Battle
    (0x720, bytes.fromhex(BLANK_DIALOGUE)),
    # Trying to Fight Blue Eyes without clearing the other bases
    (0x820, bytes.fromhex(BLANK_DIALOGUE)),
    # Lord of D. Encounter
    (0xB90, bytes.fromhex(BLANK_DIALOGUE)),
    (0xBA0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xBB0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xBC0, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Outro
    (0xC30, bytes.fromhex(BLANK_DIALOGUE)),
    (0xC40, bytes.fromhex(BLANK_DIALOGUE)),
    (0xC50, bytes.fromhex(BLANK_DIALOGUE)),
    # Alternate Mission Outro
    (0xDC0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xDD0, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0xE70, bytes.fromhex(BLANK_DIALOGUE)),
]

S15 = [
    # Pre-Mission
    (0x1F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x200, bytes.fromhex(BLANK_DIALOGUE)),
    (0x210, bytes.fromhex(BLANK_DIALOGUE)),
    (0x220, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Intro (Lumis + Umbra)
    (0x320, bytes.fromhex(BLANK_DIALOGUE)),
    (0x330, bytes.fromhex(BLANK_DIALOGUE)),
    # Ishizu Joins
    (0x4C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x500, bytes.fromhex(BLANK_DIALOGUE)),
    (0x510, bytes.fromhex(BLANK_DIALOGUE)),
    (0x520, bytes.fromhex(BLANK_DIALOGUE)),
    (0x530, bytes.fromhex(BLANK_DIALOGUE)),
    (0x540, bytes.fromhex(BLANK_DIALOGUE)),
    (0x550, bytes.fromhex(BLANK_DIALOGUE)),
    # Lumis Encounter
    (0x650, bytes.fromhex(BLANK_DIALOGUE)),
    # Umbra Encounter
    (0x6D0, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Outro
    (0x7B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x7C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x7D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x7E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x7F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x800, bytes.fromhex(BLANK_DIALOGUE)),
    (0x810, bytes.fromhex(BLANK_DIALOGUE)),
    (0x820, bytes.fromhex(BLANK_DIALOGUE)),
    (0x830, bytes.fromhex(BLANK_DIALOGUE)),
    (0x840, bytes.fromhex(BLANK_DIALOGUE)),
    # Some Alternate Ishizu text
    (0x8D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x900, bytes.fromhex(BLANK_DIALOGUE)),
    (0x910, bytes.fromhex(BLANK_DIALOGUE)),
    (0x920, bytes.fromhex(BLANK_DIALOGUE)),
    (0x930, bytes.fromhex(BLANK_DIALOGUE)),
    (0x940, bytes.fromhex(BLANK_DIALOGUE)),
    (0x950, bytes.fromhex(BLANK_DIALOGUE)),
    (0x960, bytes.fromhex(BLANK_DIALOGUE)),
    (0x970, bytes.fromhex(BLANK_DIALOGUE)),
    (0x980, bytes.fromhex(BLANK_DIALOGUE)),
    (0x990, bytes.fromhex(BLANK_DIALOGUE)),
    (0x9A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x9B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x9C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x9D0, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0xA90, bytes.fromhex(BLANK_DIALOGUE)),
]

S16 = [
    # Mokuba Cutscene
    (0x480, bytes.fromhex(BLANK_CUTSCENE)),
    # Pre-Mission
    (0x1C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1E0, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Intro
    (0x2F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x300, bytes.fromhex(BLANK_DIALOGUE)),
    (0x310, bytes.fromhex(BLANK_DIALOGUE)),
    (0x320, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Outro
    (0x410, bytes.fromhex(BLANK_DIALOGUE)),
    (0x420, bytes.fromhex(BLANK_DIALOGUE)),
    (0x430, bytes.fromhex(BLANK_DIALOGUE)),
    (0x440, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0x500, bytes.fromhex(BLANK_DIALOGUE)),
]

S17 = [
    # Face Off Cutscene
    (0x220, bytes.fromhex(BLANK_CUTSCENE)),
    # Pre-Mission
    (0x1C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1D0, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Outro
    (0x440, bytes.fromhex(BLANK_DIALOGUE)),
    (0x450, bytes.fromhex(BLANK_DIALOGUE)),
    (0x460, bytes.fromhex(BLANK_DIALOGUE)),
    (0x470, bytes.fromhex(BLANK_DIALOGUE)),
    (0x480, bytes.fromhex(BLANK_DIALOGUE)),
    (0x490, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x500, bytes.fromhex(BLANK_DIALOGUE)),
    (0x510, bytes.fromhex(BLANK_DIALOGUE)),
    (0x520, bytes.fromhex(BLANK_DIALOGUE)),
    (0x530, bytes.fromhex(BLANK_DIALOGUE)),
    (0x540, bytes.fromhex(BLANK_DIALOGUE)),
    (0x550, bytes.fromhex(BLANK_DIALOGUE)),
    (0x560, bytes.fromhex(BLANK_DIALOGUE)),
    (0x570, bytes.fromhex(BLANK_DIALOGUE)),
    # Yugi Encounter
    (0x760, bytes.fromhex(BLANK_DIALOGUE)),
    (0x770, bytes.fromhex(BLANK_DIALOGUE)),
    # Joey Encounter
    (0x7F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x800, bytes.fromhex(BLANK_DIALOGUE)),
    # Some Outro Text (Alternative)
    (0x870, bytes.fromhex(BLANK_DIALOGUE)),
    (0x880, bytes.fromhex(BLANK_DIALOGUE)),
    (0x890, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8F0, bytes.fromhex(BLANK_DIALOGUE)),
    # Long Outro
    (0x980, bytes.fromhex(BLANK_DIALOGUE)),
    (0x990, bytes.fromhex(BLANK_DIALOGUE)),
    (0x9A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x9B0, bytes.fromhex(BLANK_DIALOGUE)),
    #(0x9C0, bytes.fromhex(BLANK_DIALOGUE)),
    #(0x9D0, bytes.fromhex(BLANK_DIALOGUE)),
    #(0x9E0, bytes.fromhex(BLANK_DIALOGUE)),
    #(0x9F0, bytes.fromhex(BLANK_DIALOGUE)),
    #(0xA00, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA10, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA20, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA30, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA40, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA50, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA60, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA70, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA80, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA90, bytes.fromhex(BLANK_DIALOGUE)),
    (0xAA0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xAB0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xAC0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xAD0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xAE0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xAF0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB00, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB10, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB20, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB30, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB40, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB50, bytes.fromhex(BLANK_DIALOGUE)),
    #(0xB60, bytes.fromhex(BLANK_DIALOGUE)),
    #(0xB70, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB80, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB90, bytes.fromhex(BLANK_DIALOGUE)),
    (0xBA0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xBB0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xBC0, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0xC70, bytes.fromhex(BLANK_DIALOGUE)),
]

S18 = [
    # Saving Mokuba Cutscene
    (0xA60, bytes.fromhex(BLANK_CUTSCENE)),
    # Pre-Mission
    (0x1D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1F0, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Intro
    (0x300, bytes.fromhex(BLANK_DIALOGUE)),
    (0x310, bytes.fromhex(BLANK_DIALOGUE)),
    (0x320, bytes.fromhex(BLANK_DIALOGUE)),
    # Rescuing Mokuba
    (0x530, bytes.fromhex(BLANK_DIALOGUE)),
    (0x540, bytes.fromhex(BLANK_DIALOGUE)),
    (0x550, bytes.fromhex(BLANK_DIALOGUE)),
    (0x560, bytes.fromhex(BLANK_DIALOGUE)),
    # Scott Encounter
    (0x610, bytes.fromhex(BLANK_DIALOGUE)),
    # 05C0 - "Encountered Monsters"
    (0x780, bytes.fromhex(BLANK_DIALOGUE)),
    # Outro Text
    (0x9E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x9F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA00, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA10, bytes.fromhex(BLANK_DIALOGUE)),
    # Taking Vestora-Gate
    (0xA10, bytes.fromhex(BLANK_DIALOGUE)),
    # "Our Speedy Attack has..."
    (0xAB0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xAC0, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0xB50, bytes.fromhex(BLANK_DIALOGUE)),
    # Losing the mission
    (0xC00, bytes.fromhex(BLANK_DIALOGUE)),
    (0xC10, bytes.fromhex(BLANK_DIALOGUE)),
    (0xC20, bytes.fromhex(BLANK_DIALOGUE)),
    (0xC30, bytes.fromhex(BLANK_DIALOGUE)),
]

S19 = [
    # Pre-mission
    (0x1C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1E0, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Intro
    (0x2B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2F0, bytes.fromhex(BLANK_DIALOGUE)),
    # Odion
    (0x400, bytes.fromhex(BLANK_DIALOGUE)),
    # Fighting Odion with Ishizu
    (0x480, bytes.fromhex(BLANK_DIALOGUE)),
    (0x490, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4A0, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0x590, bytes.fromhex(BLANK_DIALOGUE)),
]

S20 = [
    # Scott Cutscene
    (0x350, bytes.fromhex(BLANK_CUTSCENE)),
    # Pre-mission
    (0x1C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1D0, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Intro
    (0x300, bytes.fromhex(BLANK_DIALOGUE)),
    (0x310, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Outro
    (0x480, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0x530, bytes.fromhex(BLANK_DIALOGUE)),
]

S21 = [
    # Final Mission Cutscenes
    (0x750, bytes.fromhex(BLANK_CUTSCENE)),
    (0x760, bytes.fromhex(BLANK_CUTSCENE)),
    (0x9F0, bytes.fromhex(BLANK_CUTSCENE)),
    (0xB30, bytes.fromhex(BLANK_CUTSCENE)),
    (0x10B0, bytes.fromhex(BLANK_CUTSCENE)),
    (0x1110, bytes.fromhex(BLANK_CUTSCENE)),
    # Pre-mission
    (0x1C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1E0, bytes.fromhex(BLANK_DIALOGUE)),
    # After defeating Scott
    (0x650, bytes.fromhex(BLANK_DIALOGUE)),
    (0x660, bytes.fromhex(BLANK_DIALOGUE)),
    (0x670, bytes.fromhex(BLANK_DIALOGUE)),
    (0x680, bytes.fromhex(BLANK_DIALOGUE)),
    (0x690, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6B0, bytes.fromhex(BLANK_DIALOGUE)),
    # Darknite
    (0x710, bytes.fromhex(BLANK_DIALOGUE)),
    # Admire your persistence?
    (0x9C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x9D0, bytes.fromhex(BLANK_DIALOGUE)),
    # Stopped the North Bridge
    (0xCC0, bytes.fromhex(BLANK_DIALOGUE)),
    # "Not recovering as quickly"
    (0xD30, bytes.fromhex(BLANK_DIALOGUE)),
    # Stopped the South Bridge
    (0xDF0, bytes.fromhex(BLANK_DIALOGUE)),
    # "Made it weaker"
    (0xE80, bytes.fromhex(BLANK_DIALOGUE)),
    # It's too powerful!
    (0xFB0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xFC0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xFD0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xFE0, bytes.fromhex(BLANK_DIALOGUE)),
    (0xFF0, bytes.fromhex(BLANK_DIALOGUE)),
    # You couldn't defeat me in a million years
    (0x11A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x11B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x11C0, bytes.fromhex(BLANK_DIALOGUE)),
    # Be glad that you were defeated by me
    (0x1230, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1240, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1250, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1260, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1270, bytes.fromhex(BLANK_DIALOGUE)),
    # Eternal Sleep
    (0x12E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x12F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1300, bytes.fromhex(BLANK_DIALOGUE)),
]

S22 = [
    # Story Ending Cutscene
    (0x1A0, bytes.fromhex(BLANK_CUTSCENE)),
]

J01 = [
    # Opening Cutscene
    (0x250, bytes.fromhex(BLANK_CUTSCENE)),
    # Pre-Mission
    (0x2B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2C0, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Intro
    (0x390, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3B0, bytes.fromhex(BLANK_DIALOGUE)),
    # Boss encounter
    (0x500, bytes.fromhex(BLANK_DIALOGUE)),
    # 05C0 - "Encountered Monsters"
    (0x630, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Outro
    (0x7B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x7C0, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0x870, bytes.fromhex(BLANK_DIALOGUE)),
]

J02 = [
    # Pre-Mission
    (0x1C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1F0, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Intro
    (0x2E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x300, bytes.fromhex(BLANK_DIALOGUE)),
    (0x310, bytes.fromhex(BLANK_DIALOGUE)),
    # 05C0 - "Encountered Monsters"
    (0x500, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Outro
    (0x680, bytes.fromhex(BLANK_DIALOGUE)),
    (0x690, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6F0, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0x7A0, bytes.fromhex(BLANK_DIALOGUE)),
]

J03 = [
    # Pre-Mission
    (0x1F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x200, bytes.fromhex(BLANK_DIALOGUE)),
    (0x210, bytes.fromhex(BLANK_DIALOGUE)),
    (0x220, bytes.fromhex(BLANK_DIALOGUE)),
    (0x230, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Intro
    (0x2F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x300, bytes.fromhex(BLANK_DIALOGUE)),
    (0x310, bytes.fromhex(BLANK_DIALOGUE)),
    # 05C0 - "Encountered Monsters"
    (0x510, bytes.fromhex(BLANK_DIALOGUE)),
    # Reinforcements Arrive
    (0x6E0, bytes.fromhex(BLANK_DIALOGUE)),
    # Reinforcements Arrive 2
    (0x7D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x7E0, bytes.fromhex(BLANK_DIALOGUE)),
    # Another dialogue line?
    (0x880, bytes.fromhex(BLANK_DIALOGUE)),
    # Tristan Arrives
    (0x8D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x8F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x900, bytes.fromhex(BLANK_DIALOGUE)),
    (0x910, bytes.fromhex(BLANK_DIALOGUE)),
    (0x920, bytes.fromhex(BLANK_DIALOGUE)),
    (0x930, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Outro Tristan Shows Up
    (0xB20, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB30, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB40, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB50, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB60, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB70, bytes.fromhex(BLANK_DIALOGUE)),
    (0xB80, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Outro Win before Tristan Shows Up
    (0xC20, bytes.fromhex(BLANK_DIALOGUE)),
    (0xC30, bytes.fromhex(BLANK_DIALOGUE)),
    (0xC40, bytes.fromhex(BLANK_DIALOGUE)),
    (0xC50, bytes.fromhex(BLANK_DIALOGUE)),
    (0xC60, bytes.fromhex(BLANK_DIALOGUE)),
    (0xC70, bytes.fromhex(BLANK_DIALOGUE)),
    (0xC80, bytes.fromhex(BLANK_DIALOGUE)),
    (0xC90, bytes.fromhex(BLANK_DIALOGUE)),
    (0xCA0, bytes.fromhex(BLANK_DIALOGUE)),
    # Lose the mission?
    (0xD50, bytes.fromhex(BLANK_DIALOGUE)),
    (0xD60, bytes.fromhex(BLANK_DIALOGUE)),
    (0xD70, bytes.fromhex(BLANK_DIALOGUE)),
]

J04 = [
    # Pre-Mission
    (0x1C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1F0, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Intro
    (0x2F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x300, bytes.fromhex(BLANK_DIALOGUE)),
    (0x310, bytes.fromhex(BLANK_DIALOGUE)),
    # Odion Encounter
    (0x420, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Outro
    (0x480, bytes.fromhex(BLANK_DIALOGUE)),
    (0x490, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4C0, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0x570, bytes.fromhex(BLANK_DIALOGUE)),
]

J05 = [
    # Pre-Mission
    (0x1F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x200, bytes.fromhex(BLANK_DIALOGUE)),
    (0x210, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Intro
    (0x320, bytes.fromhex(BLANK_DIALOGUE)),
    (0x330, bytes.fromhex(BLANK_DIALOGUE)),
    (0x340, bytes.fromhex(BLANK_DIALOGUE)),
    (0x350, bytes.fromhex(BLANK_DIALOGUE)),
    # Gemini Elf Kachua
    (0x4A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x500, bytes.fromhex(BLANK_DIALOGUE)),
    # Mai Arrives
    (0x690, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6B0, bytes.fromhex(BLANK_DIALOGUE)),
    #(0x6C0, bytes.fromhex(BLANK_DIALOGUE)),
    #(0x6D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x700, bytes.fromhex(BLANK_DIALOGUE)),
    (0x710, bytes.fromhex(BLANK_DIALOGUE)),
    (0x720, bytes.fromhex(BLANK_DIALOGUE)),
    (0x730, bytes.fromhex(BLANK_DIALOGUE)),
    (0x740, bytes.fromhex(BLANK_DIALOGUE)),
    (0x750, bytes.fromhex(BLANK_DIALOGUE)),
    # Marik Encounter
    (0x8F0, bytes.fromhex(BLANK_DIALOGUE)),
    # Ishizu Encounter
    (0x970, bytes.fromhex(BLANK_DIALOGUE)),
    # Odion Encounter
    (0x9F0, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Outro
    (0xA60, bytes.fromhex(BLANK_DIALOGUE)),
    (0xA70, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0xB40, bytes.fromhex(BLANK_DIALOGUE)),
    # 0B6B, and other comms, idk
    (0xC10, bytes.fromhex(BLANK_DIALOGUE)),
    (0xC20, bytes.fromhex(BLANK_DIALOGUE)),
    (0xC30, bytes.fromhex(BLANK_DIALOGUE)),
    (0xC40, bytes.fromhex(BLANK_DIALOGUE)),
]

J06 = [
    # Pre-Mission
    (0x1C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1F0, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Intro
    (0x2D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x300, bytes.fromhex(BLANK_DIALOGUE)),
    (0x310, bytes.fromhex(BLANK_DIALOGUE)),
    (0x320, bytes.fromhex(BLANK_DIALOGUE)),
    (0x330, bytes.fromhex(BLANK_DIALOGUE)),
    (0x340, bytes.fromhex(BLANK_DIALOGUE)),
    (0x350, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Outro
    (0x420, bytes.fromhex(BLANK_DIALOGUE)),
    (0x430, bytes.fromhex(BLANK_DIALOGUE)),
    (0x440, bytes.fromhex(BLANK_DIALOGUE)),
    (0x450, bytes.fromhex(BLANK_DIALOGUE)),
    (0x460, bytes.fromhex(BLANK_DIALOGUE)),
    (0x470, bytes.fromhex(BLANK_DIALOGUE)),
    (0x480, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0x530, bytes.fromhex(BLANK_DIALOGUE)),
]

J07 = [
    # Pre-Mission
    (0x200, bytes.fromhex(BLANK_DIALOGUE)),
    (0x210, bytes.fromhex(BLANK_DIALOGUE)),
    (0x220, bytes.fromhex(BLANK_DIALOGUE)),
    (0x230, bytes.fromhex(BLANK_DIALOGUE)),
    (0x240, bytes.fromhex(BLANK_DIALOGUE)),
    (0x250, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Intro
    (0x390, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3B0, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Outro
    (0x490, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x500, bytes.fromhex(BLANK_DIALOGUE)),
    (0x510, bytes.fromhex(BLANK_DIALOGUE)),
    (0x520, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0x5D0, bytes.fromhex(BLANK_DIALOGUE)),
]

J08 = [
    # Pre-Mission
    (0x1C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1F0, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Intro
    (0x2E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x300, bytes.fromhex(BLANK_DIALOGUE)),
    # Ishizu Encounter
    (0x460, bytes.fromhex(BLANK_DIALOGUE)),
    # Odion Encounter
    (0x4E0, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Outro
    (0x540, bytes.fromhex(BLANK_DIALOGUE)),
    (0x550, bytes.fromhex(BLANK_DIALOGUE)),
    # Lose the mission
    (0x6A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x6C0, bytes.fromhex(BLANK_DIALOGUE)),
]

J09 = [
    # Marik Cutscenes
    (0x230, bytes.fromhex(BLANK_CUTSCENE)),
    (0x420, bytes.fromhex(BLANK_CUTSCENE)),
    # Pre-Mission
    (0x1C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1D0, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Intro
    (0x3E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x3F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x400, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Outro
    (0x470, bytes.fromhex(BLANK_DIALOGUE)),
    (0x480, bytes.fromhex(BLANK_DIALOGUE)),
    (0x490, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x4B0, bytes.fromhex(BLANK_DIALOGUE)),
    # 05BF - Mission Failure
    (0x5D0, bytes.fromhex(BLANK_DIALOGUE)),
]

J10 = [
    # Kaiba Cutscene
    (0x2E0, bytes.fromhex(BLANK_CUTSCENE)),
    # Pre-Mission
    (0x1C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1E0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x1F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x200, bytes.fromhex(BLANK_DIALOGUE)),
    (0x210, bytes.fromhex(BLANK_DIALOGUE)),
    # Kaiba Encounter
    (0x470, bytes.fromhex(BLANK_DIALOGUE)),
    (0x480, bytes.fromhex(BLANK_DIALOGUE)),
    # 05C0 - "Encountered Monsters"
    (0x5A0, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Outro - Joey Wins
    (0x720, bytes.fromhex(BLANK_DIALOGUE)),
    (0x730, bytes.fromhex(BLANK_DIALOGUE)),
    (0x740, bytes.fromhex(BLANK_DIALOGUE)),
    (0x750, bytes.fromhex(BLANK_DIALOGUE)),
    (0x760, bytes.fromhex(BLANK_DIALOGUE)),
    (0x770, bytes.fromhex(BLANK_DIALOGUE)),
    (0x780, bytes.fromhex(BLANK_DIALOGUE)),
    (0x790, bytes.fromhex(BLANK_DIALOGUE)),
    (0x7A0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x7B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x7C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x7D0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x7E0, bytes.fromhex(BLANK_DIALOGUE)),
    # Mission Outro - Joey Loses
    (0x860, bytes.fromhex(BLANK_DIALOGUE)),
    (0x870, bytes.fromhex(BLANK_DIALOGUE)),
    (0x880, bytes.fromhex(BLANK_DIALOGUE)),
    (0x890, bytes.fromhex(BLANK_DIALOGUE)),
]

J11 = [
    # Basically all the cutscenes in Joey Outro
    (0x1F0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x200, bytes.fromhex(BLANK_DIALOGUE)),
    (0x210, bytes.fromhex(BLANK_DIALOGUE)),
    (0x220, bytes.fromhex(BLANK_DIALOGUE)),
    (0x230, bytes.fromhex(BLANK_DIALOGUE)),
    (0x240, bytes.fromhex(BLANK_DIALOGUE)),
    (0x250, bytes.fromhex(BLANK_DIALOGUE)),
    (0x260, bytes.fromhex(BLANK_DIALOGUE)),
    (0x270, bytes.fromhex(BLANK_DIALOGUE)),
    (0x280, bytes.fromhex(BLANK_DIALOGUE)),
    (0x290, bytes.fromhex(BLANK_DIALOGUE)),
    #(0x2A0, bytes.fromhex(BLANK_DIALOGUE)),
    #(0x2B0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2C0, bytes.fromhex(BLANK_DIALOGUE)),
    (0x2D0, bytes.fromhex(BLANK_DIALOGUE)),
]
