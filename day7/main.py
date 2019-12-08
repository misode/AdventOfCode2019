
class IntComputer:
    parameters = {
        1: [1, 1, 0],
        2: [1, 1, 0],
        3: [0],
        4: [1],
        5: [1, 1],
        6: [1, 1],
        7: [1, 1, 0],
        8: [1, 1, 0],
        99: []
    }
    instructions = {
        1: lambda self, a, b, c: self.binaryOp(1, a, b, c),
        2: lambda self, a, b, c: self.binaryOp(2, a, b, c),
        3: lambda self, a: self.readInput(a),
        4: lambda self, a: self.writeOutput(a),
        5: lambda self, a, b: self.jumpIf(a, b),
        6: lambda self, a, b: self.jumpIf(not a, b),
        7: lambda self, a, b, c: self.compare(a < b, c),
        8: lambda self, a, b, c: self.compare(a == b, c),
        99: lambda self: self.halt()
    }

    def __init__(self, code, input=[], output=[]):
        self.code = code
        self.i = 0
        self.running = True
        self.input = input
        self.output = output

    def binaryOp(self, opcode, a, b, c):
        #print("op", a, b)
        self.code[c] = a + b if opcode == 1 else a * b
        self.i += 4

    def readInput(self, a):
        #print("read", a)
        self.code[a] = self.input.pop()
        self.i += 2

    def writeOutput(self, a):
        #print("write", a)
        self.output.append(a)
        self.i += 2

    def jumpIf(self, condition, b):
        #print("jump", condition, b)
        self.i = b if condition else self.i + 3

    def compare(self, condition, c):
        #print("compare", condition, c)
        self.code[c] = 1 if condition else 0
        self.i += 4

    def halt(self):
        self.running = False

    def cycle(self):
        if not self.running:
            return
        cc = "0000" + str(self.code[self.i])
        opcode = int(cc[-2:])
        args = []
        #print(self.i, self.code)
        for i, p in enumerate(self.parameters[opcode]):
            mode = int(cc[-3-i:-2-i])
            arg = self.code[self.i + i + 1]
            if p and mode == 0:
                arg = self.code[arg]
            args.append(arg)
        #print(opcode, args, "-> ", end="")
        return self.instructions[opcode](self, *args)

    def run(self):
        while self.running:
            self.cycle()

def runComputer(code, input=[], output=[]):
    inputProvided = bool(input)
    computer = IntComputer(code, input, output)
    computer.run()
    return computer.output

print("--- Answers ---")
with open("day7/in.txt", "r") as f:
    code = [int(i) for i in f.readline().split(",")]

