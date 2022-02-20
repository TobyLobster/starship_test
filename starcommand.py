#########################################################################################
#
# Starship Command disassembler
#
#########################################################################################

from commands import *
import acorn

load(0x1f00, "ORIGINAL_DISK/COMM2#.bin")

acorn.mos_labels()
acorn.hardware_bbc()


# Relocate code
move(0x0e00, 0x1f00, 0x42b0)

# Memory locations
entry(0x61b1, "entry_point")

go()
