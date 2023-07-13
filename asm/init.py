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



# 1.プログラム中で指定した 10 進数 1 桁の数値を 7 セグ LED に表示するプログラムを作成する．

def init(r1, r2):
    program = [
        'start',
        Inst.LUI(29, 0x10000000), # 7seg_num_offset
        Inst.LUI(30, 0x04000000), # display_offset
        Inst.LUI(31, 0x10000100), # dot_num_offset
        Inst.ADDI(r1, 0, seg[0]), # 7seg: 0
        Inst.SB(29, r1, 0x0),
        Inst.ADDI(r1, 0, seg[1]), # 1
        Inst.SB(29, r1, 0x1),
        Inst.ADDI(r1, 0, seg[2]), # 2
        Inst.SB(29, r1, 0x2),
        Inst.ADDI(r1, 0, seg[3]), # 3
        Inst.SB(29, r1, 0x3),
        Inst.ADDI(r1, 0, seg[4]), # 4
        Inst.SB(29, r1, 0x4),
        Inst.ADDI(r1, 0, seg[5]), # 5
        Inst.SB(29, r1, 0x5),
        Inst.ADDI(r1, 0, seg[6]), # 6
        Inst.SB(29, r1, 0x6),
        Inst.ADDI(r1, 0, seg[7]), # 7
        Inst.SB(29, r1, 0x7),
        Inst.ADDI(r1, 0, seg[8]), # 8
        Inst.SB(29, r1, 0x8),
        Inst.ADDI(r1, 0, seg[9]), # 9
        Inst.SB(29, r1, 0x9),
        Inst.ADDI(r1, 0, seg['A']), # A
        Inst.SB(29, r1, 0xA),
        Inst.ADDI(r1, 0, seg['B']), # A
        Inst.SB(29, r1, 0xB),
        Inst.ADDI(r1, 0, seg['C']), # A
        Inst.SB(29, r1, 0xC),
        Inst.ADDI(r1, 0, seg['D']), # A
        Inst.SB(29, r1, 0xD),
        Inst.ADDI(r1, 0, seg['E']), # A
        Inst.SB(29, r1, 0xE),
        Inst.ADDI(r1, 0, seg['F']), # A
        Inst.SB(29, r1, 0xF),

        # プレイヤー表示
        Inst.ADDI(r2, 0, seg['A']),
        Inst.SB(30, r2, 0x00),
        Inst.ADDI(r2, 0, seg['B']),
        Inst.SB(30, r2, 0x10),
        Inst.ADDI(r2, 0, seg['C']),
        Inst.SB(30, r2, 0x20),
        Inst.ADDI(r2, 0, seg['D']),
        Inst.SB(30, r2, 0x30),
        # dot表示
        Inst.ADDI(r2, 0, 0x01),
        Inst.SB(30, r2, 0x40),
        Inst.SB(30, r2, 0x42),
        Inst.SB(30, r2, 0x44),
        Inst.SB(30, r2, 0x46),
        
        # test
        Inst.ADD(7, 0, 0), # x7 = 0 (1 digit counter)
        'loop',
        Inst.ADD(8, 7, 29), # address of memory[x7]
        Inst.LBU(9, 8, 0), # x9 = memory[x7]
        Inst.SB(30, 9, 0x01), # 7seg で表示
        Inst.ADDI(7, 7, 1), # x7++
        Inst.LJAL(0, 'loop') # goto loop
    ]
    return program

# def display_dotmatrix(reg_mem_addr, reg_offset, reg, reg2, reg3, reg_A, reg_B, reg_C, reg_D, offset=0x04000000, mem_addr=0x10001000):
#     program = [
#         'start',
#         Inst.LUI(reg_mem_addr, mem_addr), # memory = 0x10001000
#         Inst.ADDI(reg, 0, 0b00000001),
#         Inst.SB(reg_mem_addr, reg, 0x0),
#         Inst.ADDI(reg, 0, 0b00000010),
#         Inst.SB(reg_mem_addr, reg, 0x1),
#         Inst.ADDI(reg, 0, 0b00000100),
#         Inst.SB(reg_mem_addr, reg, 0x2),
#         Inst.ADDI(reg, 0, 0b00001000),
#         Inst.SB(reg_mem_addr, reg, 0x3),
#         Inst.ADDI(reg, 0, 0b00010000),
#         Inst.SB(reg_mem_addr, reg, 0x4),
#         Inst.ADDI(reg, 0, 0b00100000),
#         Inst.SB(reg_mem_addr, reg, 0x5),
#         Inst.ADDI(reg, 0, 0b01000000),
#         Inst.SB(reg_mem_addr, reg, 0x6),
#         Inst.ADDI(reg, 0, 0b10000000),
#         Inst.SB(reg_mem_addr, reg, 0x7),
#         # dot表示
#         Inst.LUI(reg_offset, offset),
#         # 仮にreg_Aに0x5を入れる
#         Inst.ADDI(reg_A, 0, 0x05),
#         Inst.ADD(reg2, reg_A, reg_mem_addr),
#         Inst.LBU(reg3, reg2, 0),
#         Inst.SB(reg_offset, reg3, 0x40),
#     ]
#     return program

r = asm(init(1, 2))
print_asm(r)
print()
print_ihex(r)