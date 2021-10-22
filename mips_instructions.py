import random

MIPS_INSTRUCTIONS   = []
MIPS_R_INSTRUCTIONS = []
MIPS_I_INSTRUCTIONS = []
MIPS_I_ARITH_INSTRUCTIONS = []
MIPS_I_MEM_INSTRUCTIONS = []
MIPS_J_INSTRUCTIONS = []

class MIPSInstruction:
    def __str__(self):
        return self.asm

    __repr__ = __str__

    def __init__(self):
        self.name = "Instruction"
        self.asm = "instr"
        self.write_rf = False
        self.read_rf  = False
        self.read_mem = False
        self.write_mem= False
        self.use_alu  = False
        self.mod_pc   = False
        self.is_load  = False
        self.is_store = False
        self.is_arithmetic = False
        self.is_branch= False
        self.is_jump  = False

class IFormatInstruction(MIPSInstruction):
    def __str__(self):
        if self.read_mem or self.write_mem:
            return self.asm + " " + str(self.rt) + ", " + str(self.rs) + "(" + str(self.imm) + ")"
        else:
            return self.asm + " " + str(self.rt) + ", " + str(self.rs) + ", " + str(self.imm)

    def __init__(self, rt, rs, imm):
        super().__init__()
        self.rt = rt
        self.rs = rs
        self.imm = imm
        self.read_rf = True
        self.use_alu = True

class JFormatInstruction(MIPSInstruction):
    def __str__(self):
        return self.asm + " " + str(self.off)

    def __init__(self, off):
        super().__init__()
        self.off = off
        self.mod_pc = True
        self.is_jump = True

class RFormatInstruction(MIPSInstruction):
    def __str__(self):
        return self.asm + " " + str(self.rd) + ", " + str(self.rs) + ", " + str(self.rt)

    def __init__(self, rd, rs, rt):
        super().__init__()
        self.rd = rd
        self.rs = rs
        self.rt = rt
        self.use_alu = True
        self.read_rf = True
        self.write_rf = True

MIPS_INSTRUCTION_FORMATS = [RFormatInstruction, IFormatInstruction, JFormatInstruction]

def get_random_i_format_instruction():
    return random.choice(MIPS_I_INSTRUCTIONS)

def get_random_j_format_instruction():
    return random.choice(MIPS_J_INSTRUCTIONS)

def get_random_r_format_instruction():
    return random.choice(MIPS_R_INSTRUCTIONS)

def get_random_instruction():
    return random.choice(MIPS_INSTRUCTIONS)

def get_random_format():
    return random.choice(MIPS_INSTRUCTION_FORMATS)

# R Format instructions (rd, rs, rt)
class AddSigned(RFormatInstruction):
    def __init__(self, rd, rs, rt):
        super().__init__(rd, rs, rt)
        self.asm = "add"

class AddUnsigned(RFormatInstruction):
    def __init__(self, rd, rs, rt):
        super().__init__(rd, rs, rt)
        self.asm = "addu"

class AndBitwise(RFormatInstruction):
    def __init__(self, rd, rs, rt):
        super().__init__(rd, rs, rt)
        self.asm = "and"

class OrBitwise(RFormatInstruction):
    def __init__(self, rd, rs, rt):
        super().__init__(rd, rs, rt)
        self.asm = "or"

class ShiftLogicalLeft(RFormatInstruction):
    def __init__(self, rd, rs, rt):
        super().__init__(rd, rs, rt)
        self.asm = "sll"

class ShiftLogicalRight(RFormatInstruction):
    def __init__(self, rd, rs, rt):
        super().__init__(rd, rs, rt)
        self.asm = "slr"

class SetLessThan(RFormatInstruction):
    def __init__(self, rd, rs, rt):
        super().__init__(rd, rs, rt)
        self.asm = "slt"

MIPS_R_INSTRUCTIONS = [AddSigned, AddUnsigned, AndBitwise, OrBitwise, ShiftLogicalLeft, ShiftLogicalRight, SetLessThan]

# I Format Instructions (rt, rs, imm)
class AddImmediateSigned(IFormatInstruction):
    def __init__(self, rt, rs, imm):
        super().__init__(rt, rs, imm)
        self.asm = "addi"
        self.write_rf = True

class AddImmediateUnsigned(IFormatInstruction):
    def __init__(self, rt, rs, imm):
        super().__init__(rt, rs, imm)
        self.asm = "addiu"
        self.write_rf = True

class AndBitwiseImmediate(IFormatInstruction):
    def __init__(self, rt, rs, imm):
        super().__init__(rt, rs, imm)
        self.asm = "andi"
        self.write_rf = True

class OrBitwiseImmediate(IFormatInstruction):
    def __init__(self, rt, rs, imm):
        super().__init__(rt, rs, imm)
        self.asm = "ori"
        self.write_rf = True

class LoadUpperImmediate(IFormatInstruction):
    def __init__(self, rt, rs, imm):
        super().__init__(rt, rs, imm)
        self.asm = "lui"
        self.write_rf = True
        self.read_rf = False

class LoadWord(IFormatInstruction):
    def __init__(self, rt, rs, imm):
        super().__init__(rt, rs, imm)
        self.asm = "lw"
        self.read_mem = True
        self.write_rf = True

class StoreWord(IFormatInstruction):
    def __init__(self, rt, rs, imm):
        super().__init__(rt, rs, imm)
        self.asm = "sw"
        self.write_mem = True

class BranchEqual(IFormatInstruction):
    def __init__(self, rt, rs, imm):
        super().__init__(rt, rs, imm)
        self.asm = "beq"
        self.mod_pc = True

class BranchNotEqual(IFormatInstruction):
    def __init__(self, rt, rs, imm):
        super().__init__(rt, rs, imm)
        self.asm = "bne"
        self.mod_pc = True

MIPS_I_ARITH_INSTRUCTIONS = [AddImmediateSigned, AddImmediateUnsigned, AndBitwiseImmediate, OrBitwiseImmediate, LoadUpperImmediate]
MIPS_I_MEM_INSTRUCTIONS = [LoadWord, StoreWord]
MIPS_I_INSTRUCTIONS = MIPS_I_ARITH_INSTRUCTIONS + MIPS_I_MEM_INSTRUCTIONS + [BranchEqual, BranchNotEqual, LoadUpperImmediate]

# J Format Instructions (off)
class Jump(JFormatInstruction):
    def __init__(self, offset):
        super().__init__(offset)
        self.asm = "j"

class JumpAndLink(JFormatInstruction):
    def __init__(self, offset):
        super().__init__(offset)
        self.asm = "jal"

MIPS_J_INSTRUCTIONS = [Jump, JumpAndLink]

MIPS_INSTRUCTIONS = MIPS_R_INSTRUCTIONS + MIPS_I_INSTRUCTIONS + MIPS_J_INSTRUCTIONS
