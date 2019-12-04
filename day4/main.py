import timeit

# My imput range starts before 111111 so I don't need to worry about to lower bound
inputRange = (109165, 576723)
[A, B, C, D, E, F] = [int(i) for i in str(inputRange[1])]

optionsPart1 = 0
optionsPart2 = 0

for a in range(1, 10):
    if a > A:
        continue
    for b in range(a, 10):
        if a == A and b > B:
            continue
        for c in range(b, 10):
            if a == A and b == B and c > C:
                continue
            for d in range(c, 10):
                if a == A and b == B and c == C and d > D:
                    continue
                for e in range(d, 10):
                    if a == A and b == B and c == C and d == D and e > E:
                        continue
                    for f in range(e, 10):
                        if a == A and b == B and c == C and d == D and e == E and f > F:
                            continue
                        if a != b and b != c and c != d and d != e and e != f:
                            continue
                        optionsPart1 += 1
                        if (a == b and b != c) or (a != b and b == c and c != d) or (b != c and c == d and d != e) or (c != d and d == e and e != f) or (d != e and e == f):
                            optionsPart2 += 1

print(f"--- Answers ---")
print(f"Part 1: {optionsPart1}")
print(f"Part 2: {optionsPart2}")
