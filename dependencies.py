class DataDependency():
    def __str__(self):
        return self.type + " Dependency between instr #" + str(self.first) + " and instr #" + str(self.last)

    __repr__ = __str__

    def __init__(self):
        self.type = "Generic"
        self.first = 0
        self.last = 1

class RAWDependency(DataDependency):
    def __init__(self, write_instr_num, read_instr_num):
        super().__init__()
        self.type = "RAW"
        self.first = write_instr_num
        self.last = read_instr_num

class WARDependency(DataDependency):
    def __init__(self, read_instr_num, write_instr_num):
        super().__init__()
        self.type = "WAR"
        self.first = read_instr_num
        self.last = write_instr_num

class WAWDependency(DataDependency):
    def __init__(self, first_write_instr_num, second_write_instr_num):
        super().__init__()
        self.type = "WAW"
        self.first = first_write_instr_num
        self.last = second_write_instr_num

class RegisterAccessHistory():
    def __init__(self, reg):
        self.reg = reg
        self.read_by = []
        self.written_by = []

class DependencyReport():
    def __init__(self):
        self.raw = []
        self.war = []
        self.waw = []
