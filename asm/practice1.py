from inst import Inst, asm, print_asm, print_ihex

seg = {
    0 : 0xFC,
    1 : 0x60,
    2 : 0xDA,
    3 : 0xF2,
    4 : 0x66,
    5 : 0xB6,
    6 : 0xBE,
    7 : 0xE0,
    8 : 0xFE,
    9 : 0xF6,
    'A' : 0xEE,
    'B' : 0x3E,
    'C' : 0x1A,
    'D' : 0x7A,
    'E' : 0x9E,
    'F' : 0x8E,
}
# 11111100,
# 01100000,
# 11011010,
# 11110010,
# 01100110,
# 10110110,
# 10111110,
# 11100000,
# 11111110,
# 11110110,
# 11101110,
# 00111110,
# 00011010,
# 01111010,
# 10011110,
# 10001110,

def calc_f():
    for i in range(16):
        print(i, ':', hex(seg[i]))
        
        
        
        
program = [
Inst.LUI(5, 0x04000000),
Inst.ADDI(10, 0, seg[1]), # 7seg に「0」を表示
Inst.SB(5, 10, 0x00),
Inst.JAL(0, -4*2)
]

calc = [
    'start',
    Inst.LUI(5, 0x04000000),
    Inst.ADDI(6, 0, 0xFF),
    Inst.LW(10, 5, 0x48),
    Inst.ANDI(11, 10, 0x01),
    Inst.BEQ(11, 0, 0x08),
    #
    Inst.LUI(5, 0x04000000),
    Inst.ADDI(0, 0, seg[1]),
    Inst.SB(0, 0, 0x000),
    Inst.LJAL(0, 'end'),
    #
    'end',
    Inst.JAL(0, 'start')
]

r = asm(program)
print_asm(r)
print()
print_ihex(r)