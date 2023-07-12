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

def init(reg_mem_addr, reg, offset=0x04000000):
    program = [
        'start',
        Inst.LUI(reg_mem_addr, offset),
        Inst.ADDI(reg, 0, seg['A']),
        Inst.SB(reg_mem_addr, reg, 0x00),
        Inst.ADDI(reg, 0, seg['B']),
        Inst.SB(reg_mem_addr, reg, 0x10),
        Inst.ADDI(reg, 0, seg['C']),
        Inst.SB(reg_mem_addr, reg, 0x20),
        Inst.ADDI(reg, 0, seg['D']),
        Inst.SB(reg_mem_addr, reg, 0x30),
        # dot表示
        Inst.ADDI(reg, 0, 0x01),
        Inst.SB(reg_mem_addr, reg, 0x40),
        Inst.SB(reg_mem_addr, reg, 0x42),
        Inst.SB(reg_mem_addr, reg, 0x44),
        Inst.SB(reg_mem_addr, reg, 0x46),
    ]
    return program

def display_dotmatrix(reg_mem_addr, reg_offset, reg, reg2, reg3, reg_A, reg_B, reg_C, reg_D, offset=0x04000000, mem_addr=0x10001000):
    program = [
        'start',
        Inst.LUI(reg_mem_addr, mem_addr), # memory = 0x10001000
        Inst.ADDI(reg, 0, 0b00000001),
        Inst.SB(reg_mem_addr, reg, 0x0),
        Inst.ADDI(reg, 0, 0b00000010),
        Inst.SB(reg_mem_addr, reg, 0x1),
        Inst.ADDI(reg, 0, 0b00000100),
        Inst.SB(reg_mem_addr, reg, 0x2),
        Inst.ADDI(reg, 0, 0b00001000),
        Inst.SB(reg_mem_addr, reg, 0x3),
        Inst.ADDI(reg, 0, 0b00010000),
        Inst.SB(reg_mem_addr, reg, 0x4),
        Inst.ADDI(reg, 0, 0b00100000),
        Inst.SB(reg_mem_addr, reg, 0x5),
        Inst.ADDI(reg, 0, 0b01000000),
        Inst.SB(reg_mem_addr, reg, 0x6),
        Inst.ADDI(reg, 0, 0b10000000),
        Inst.SB(reg_mem_addr, reg, 0x7),
        # dot表示
        Inst.LUI(reg_offset, offset),
        # 仮にreg_Aに0x5を入れる
        Inst.ADDI(reg_A, 0, 0x05),
        Inst.ADD(reg2, reg_A, reg_mem_addr),
        Inst.LBU(reg3, reg2, 0),
        Inst.SB(reg_offset, reg3, 0x40),
    ]
    return program




# r = asm(init(5, 10))
r = asm(display_dotmatrix(5, 6, 7, 8, 9, 10, 11, 12, 13))
print_asm(r)
print()
print_ihex(r)