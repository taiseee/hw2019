from inst import Inst, asm, print_asm, print_ihex

calc = [
    # Store 7seg led patterns
    Inst.LUI(5, 0x10001000), # memory = 0x10001000
    Inst.ADDI(6, 0, 0b11111100), # 7seg: 0
    Inst.SB(5, 6, 0x0),
    Inst.ADDI(6, 0, 0b01100000), # 1
    Inst.SB(5, 6, 0x1),
    Inst.ADDI(6, 0, 0b11011010), # 2
    Inst.SB(5, 6, 0x2),
    Inst.ADDI(6, 0, 0b11110010), # 3
    Inst.SB(5, 6, 0x3),
    Inst.ADDI(6, 0, 0b01100110), # 4
    Inst.SB(5, 6, 0x4),
    Inst.ADDI(6, 0, 0b10110110), # 5
    Inst.SB(5, 6, 0x5),
    Inst.ADDI(6, 0, 0b10111110), # 6
    Inst.SB(5, 6, 0x6),
    Inst.ADDI(6, 0, 0b11100000), # 7
    Inst.SB(5, 6, 0x7),
    Inst.ADDI(6, 0, 0b11111110), # 8
    Inst.SB(5, 6, 0x8),
    Inst.ADDI(6, 0, 0b11110110), # 9
    Inst.SB(5, 6, 0x9),
    # Main
    Inst.LUI(6, 0x04000000),
    Inst.ADD(7, 0, 0), # x7 = 0 (1 digit counter)
    Inst.ADD(12, 0, 0), # x12 = 0 (10 digit counter)
    Inst.ADDI(1, 0, 10), # x1 = 10
    'loop',
    Inst.ADD(8, 7, 5), # address of memory[x7]
    Inst.LBU(9, 8, 0), # x9 = memory[x7]
    Inst.ADD(13, 12, 5), # address of memory[x12]
    Inst.LBU(14, 13, 0), # x14 = memory[x12]
    Inst.SB(6, 9, 1), # 7seg で表示
    Inst.SB(6, 14, 0), # 7seg で表示

    Inst.LW(10, 6, 0x48), # オフセット 0x48 の値を取得
    Inst.ANDI(11, 10, 0x01), # ANDI で LSB が 1 かどうかしらべ...
    Inst.LBEQ(11, 0, 'jump'), # ANDI の結果が 0 だったら分岐
    Inst.ADDI(7, 7, 1), # x7++
    'jump',
    Inst.LBNE(7, 1, 'loop'), # x7 = 10 でないとき分岐
    Inst.ADD(7, 0, 0), # x7 = 0
    Inst.ADDI(12, 12, 1), # x12++
    Inst.LBNE(12, 1, 'loop'), # x12 = 10 でないとき分岐
    Inst.ADD(12, 0, 0), # x12 = 0
    Inst.LJAL(0, 'loop') # goto loop
]


r = asm(calc)
print_asm(r)
print()
print_ihex(r)