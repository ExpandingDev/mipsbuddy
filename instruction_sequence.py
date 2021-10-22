class InstructionSequence():

    def __str__(self):
        s = "Instruction Sequence\n"
        for j,i in enumerate(self.instructions):
            s += str(j) + "\t" + str(i) + "\n"
        return s

    __repr__ = __str__

    def execute(self):
        print("WARNING: NOT IMPLEMENTED")
        #for i in self.instructions:
        #    i.execute()

    def __init__(self, instructions):
        self.instructions = instructions
