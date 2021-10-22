import random
import math

MIPS_REGISTER_NAMES = ["zero", "at", "v0", "v1", "a0", "a1", "a2", "a3",\
"t0", "t1", "t2", "t3", "t4", "t5", "t6", "t7",\
"s0", "s1", "s2", "s3", "s4", "s5", "s6", "s7",\
"t8", "t9", "gp", "sp", "fp", "ra"]

class Register:
    def __str__(self):
        return "$" + self.name

    __repr__ = __str__

    def __init__(self, number, name):
        self.name = name
        self.number = number
        self.value = 0
        self.is_temp = name[0] == "t"

    def set(self, value):
        self.value = value

    def get(self):
        return self.value

class RegisterFile:
    def __str__(self):
        return "Register file with " + str(len(self.regs)) + " registers"

    __repr__ = __str__

    def read_register(self, reg_num, instruction_id):
        self.history[reg_num].read.append(instruction_id)
        return self.regs[reg_num].get()

    def write_register(self, reg_num, value, instruction_id):
        self.history[reg_num].write.append(instruction_id)
        self.regs[reg_num].set(value)

    def get_register(self, name):
        for reg in regs:
            if name == reg.name or "$" + name == reg.name:
                return reg

    def clear_history(self):
        for h in self.history:
            h.read = []
            h.write = []

    def __init__(self, regs):
        self.regs = regs
        self.history = []
        for r in self.regs:
            self.history.append({"read": [], "write": []})

def generate_mips_rf():
    regs = []
    register_num = 0
    for name in MIPS_REGISTER_NAMES:
        regs.append(Register(register_num, name))
        register_num = register_num + 1
    
    return RegisterFile(regs)

def get_temp_registers_from_rf(rf):
    t = []
    for reg in rf.regs:
        if reg.is_temp:
            t.append(reg)
    return t

def get_example_registers_from_rf(rf):
    t = get_temp_registers_from_rf(rf)
    for reg in rf.regs:
        if (reg.name[0] == "s" and reg.name != "sp"):
            t.append(reg)
    for reg in rf.regs:
        if  reg.name[0] == "v" or (reg.name[0] == "a" and reg.name != "at"):
            t.append(reg)
    return t

MIPS_RF = generate_mips_rf()
MIPS_TEMP_REGS = get_temp_registers_from_rf(MIPS_RF)
MIPS_EXAMPLE_REGS = get_example_registers_from_rf(MIPS_RF)
