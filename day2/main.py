

def run(code):
    i = 0
    while True:
        c = code[i]
        if c is 1:
            code[code[i+3]] = code[code[i+1]] + code[code[i+2]]
            i += 4
        elif c is 2:
            code[code[i+3]] = code[code[i+1]] * code[code[i+2]]
            i += 4
        elif c is 99:
            return code[0]
        else:
            print(f"Unknown opcode {c}")
            return None

def attempt(i, j, code):
    code[1] = i
    code[2] = j
    return run(code) == 19690720

print("--- Tests part 1 ---")
print(run([1,9,10,3,2,3,11,0,99,30,40,50]))
print(run([1,0,0,0,99]))
print(run([2,3,0,3,99]))
print(run([2,4,4,5,99,0]))
print(run([1,1,1,4,99,5,6,0,99]))

print("--- Answers ---")
with open("day2/in.txt", "r") as f:
    code = [int(i) for i in f.readline().split(",")]
    n = len(code)
    code1 = code[:]
    code1[1] = 12
    code1[2] = 1
    print(f"Part 1: {run(code1)}")
    for i in range(0, n):
        for j in range(0, n):
            if attempt(i, j, code[:]):
                print(f"noun={i}, verb={j} -> 19690720")
                print(f"Part 2: {100*i + j}")
