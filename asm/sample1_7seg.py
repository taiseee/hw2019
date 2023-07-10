from inst import Inst, asm, print_asm, print_ihex

program = [
    Inst.LUI(5, 0x04000000),  # r5 に7 セグのアドレスを代入
    Inst.ADDI(10, 0, 0x60),   # セグ「1」のパタンをr10 に代入
    Inst.SB(5, 10, 0x00),     # r5[0] = 0x60 (7 セグのアドレスに0x60 をストア)
    Inst.JAL(0, -4*1)         # 1 命令前に無条件分岐
]

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

r = asm(program)
print_asm(r)
print()
print_ihex(r)
