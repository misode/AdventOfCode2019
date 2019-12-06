
def pathToRoot(orbits, n):
    while n != "COM":
        n = orbits[n]
        yield n

with open("day6/in.txt", "r") as f:
    orbits = {j[1]: j[0] for j in [tuple(i.strip().split(')')) for i in f.readlines()]}
    print("--- Answers ---")

    count = sum([len(list(pathToRoot(orbits, k))) for k in orbits])
    print(f"Part 1: {count}")

    pathToYou = list(pathToRoot(orbits, "YOU"))
    pathToSan = list(pathToRoot(orbits, "SAN"))
    i = 1
    while pathToYou[-i] == pathToSan[-i]:
        i += 1
    print(f"Path 2: {len(pathToYou) + len(pathToSan) - 2*i + 2}")
