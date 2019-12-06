

def run(code, input=[], output=[]):
    i = 0
    while True:
        c = "0000" + str(code[i])
        op = int(c[-2:])
        m1 = int(c[-3:-2])
        m2 = int(c[-4:-3])
        m3 = int(c[-5:-4])
        if op is 1:
            a = code[(i+1 if m1 else code[i+1])]
            b = code[(i+2 if m2 else code[i+2])]
            code[code[i+3]] = a + b
            i += 4
        elif op is 2:
            a = code[(i+1 if m1 else code[i+1])]
            b = code[(i+2 if m2 else code[i+2])]
            code[code[i+3]] = a * b
            i += 4
        elif op is 3:
            code[code[i+1]] = input.pop()
            i += 2
        elif op is 4:
            a = code[(i+1 if m1 else code[i+1])]
            output.append(a)
            i += 2
        elif op is 5:
            a = code[(i+1 if m1 else code[i+1])]
            b = code[(i+2 if m2 else code[i+2])]
            if a:
                i = b
            else:
                i += 2
        elif op is 6:
            a = code[(i+1 if m1 else code[i+1])]
            b = code[(i+2 if m2 else code[i+2])]
            if not a:
                i = b
            else:
                i += 2
        elif op is 7:
            a = code[(i+1 if m1 else code[i+1])]
            b = code[(i+2 if m2 else code[i+2])]
            if a < b:
                code[i+3] = 1
        elif op is 8:
            a = code[(i+1 if m1 else code[i+1])]
            b = code[(i+2 if m2 else code[i+2])]
            if a == b:
                code[i+3] = 1
        elif op is 99:
            return output
        else:
            print(f"Unknown opcode {c}")
            return output

print("--- Tests part 1 ---")
print(run([3,0,4,0,99], [5], []))
print(run([1002,4,3,4,33], [], []))

print("--- Tests part 2 ---")
print(run([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], [0], []))
print(run([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], [1], []))
print(run([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], [0], []))
print(run([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], [1], []))

print("--- Answers ---")
with open("day5/in.txt", "r") as f:
    code = [int(i) for i in f.readline().split(",")]
    print(f"Part 1: {run(code, input=[1])}")
    print(f"Part 1: {run(code, input=[5])}")
