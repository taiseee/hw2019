from inst import Inst, asm, print_asm, print_ihex


def timer(r1,r2,r3,r4):
    program = [
        Inst.LUI(r1, 0x02000000),
        Inst.LUI(r2, 0x10000200),
        Inst.LW(r3, r1, 0x4),
        Inst.SW(r2, r3, 0x104),
        Inst.LW(r3, r1, 0x0),
        Inst.SW(r2, r3, 0x100),
        Inst.LW(r3, r1, 0x4),
        Inst.JAL(0, -4*5)
        # Inst.LBEQ(r3, r4, 'loop'),
    ]
    
    return program


r = asm(timer(1,2,3,4))
print_asm(r)
print()
print_ihex(r)