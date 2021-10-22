import mips_instructions as mi
import mips_registers as mr
from instruction_sequence import InstructionSequence

import random

# Probabilities of each instruction type in our sequences
r_mix = 0.5
i_arith_mix = 0.15
load_mix = 0.18
store_mix = 0.12
branch_mix = 0.049
j_mix = 0.001

DEFAULT_INSTRUCTION_MIX = [r_mix, i_arith_mix, load_mix, store_mix, branch_mix, j_mix]
INSTRUCTION_MIX_TYPES = [mi.RFormatInstruction, mi.IFormatInstruction, mi.LoadWord, mi.StoreWord, mi.BranchEqual, mi.JFormatInstruction]

def generate_random_sequence(mix, count, registers):
    instruction_types = random.choices(INSTRUCTION_MIX_TYPES, weights=mix, k=count)
    s = InstructionSequence([])
    for i,t in enumerate(instruction_types):
        rd = random.choice(registers)
        rs = random.choice(registers)
        rt = random.choice(registers)
        val = random.randrange(0, 64, 8)
        if t == mi.RFormatInstruction:
            s.instructions.append(mi.get_random_r_format_instruction()(rd, rs, rt))
        elif t == mi.JFormatInstruction:
            s.instructions.append(mi.get_random_j_format_instruction()("Label1"))
        elif t == mi.IFormatInstruction: # choose a random arithmetic I instruction
            s.instructions.append(random.choice(mi.MIPS_I_ARITH_INSTRUCTIONS)(rs, rt, val))
        elif t == mi.BranchEqual: # choose a random branch
            s.instructions.append(random.choice([mi.BranchEqual, mi.BranchNotEqual])(rt, rs, "Label1"))
        else: # is either LoadWord or StoreWord
            s.instructions.append(t(rt, rs, val))
    return s

def generate_random_example_sequence(mix, count, register_count):
    return generate_random_sequence(mix, count, mr.MIPS_EXAMPLE_REGS[:register_count])
