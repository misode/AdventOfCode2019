
def createWireSet(instructions):
    def runInstruction(dir, length):
        for j in range(1, length+1):
            wire.add((x + dir[0]*j, y + dir[1]*j))

    wire = set()
    x = 0
    y = 0
    for i in instructions:
        direction = i[0]
        length = int(i[1:])
        if direction is "U":
            runInstruction((0, -1), length)
            y -= length
        elif direction is "D":
            runInstruction((0, 1), length)
            y += length
        elif direction is "L":
            runInstruction((-1, 0), length)
            x -= length
        elif direction is "R":
            runInstruction((1, 0), length)
            x += length
    return wire

def createWireMap(instructions):
    def runInstruction(dist, dir, length):
        for j in range(1, length+1):
            pos = (x + dir[0]*j, y + dir[1]*j)
            dist += 1
            wire[pos] = wire.get(pos, dist)
        return dist

    wire = dict()
    dist = 0
    x = 0
    y = 0
    for i in instructions:
        direction = i[0]
        length = int(i[1:])
        if direction is "U":
            dist = runInstruction(dist, (0, -1), length)
            y -= length
        elif direction is "D":
            dist = runInstruction(dist, (0, 1), length)
            y += length
        elif direction is "L":
            dist = runInstruction(dist, (-1, 0), length)
            x -= length
        elif direction is "R":
            dist = runInstruction(dist, (1, 0), length)
            x += length
    return wire

with open("day3/in.txt", "r") as f:
    w1 = f.readline().split(",")
    w2 = f.readline().split(",")

    print(f"--- Answers ---")

    wireSet1 = createWireSet(w1)
    wireSet2 = createWireSet(w2)

    intersectionPart1 = wireSet1.intersection(wireSet2)
    summed = [abs(i)+abs(j) for (i, j) in intersectionPart1]
    print(f"Part 1: {min(summed)}")

    wireMap1 = createWireMap(w1)
    wireMap2 = createWireMap(w2)

    intersectionPart2 = wireMap1.keys() & wireMap2.keys()
    mindist = 10000000000
    for i in intersectionPart2:
        mindist = min(wireMap1[i] + wireMap2[i], mindist)
    print(f"Part 2: {mindist}")
