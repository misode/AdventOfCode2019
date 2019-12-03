
def fuel(mass):
    return int(mass/3) - 2

def totalFuel(mass):
    total = 0
    while mass > 0:
        mass = fuel(mass)
        if mass < 0:
            mass = 0
        total += mass
    return total

print("--- Tests part 1 ---")
print(fuel(12))
print(fuel(14))
print(fuel(1969))
print(fuel(100756))

print("--- Tests part 2 ---")
print(totalFuel(14))
print(totalFuel(1969))
print(totalFuel(100756))

print("--- Answers ---")

with open("day1/in.txt", "r") as f:
    data = f.readlines();
    fuels = [fuel(int(i)) for i in data]
    totalFuels = [totalFuel(int(i)) for i in data]
    print(f"Part 1: {sum(fuels)}")
    print(f"Part 2: {sum(totalFuels)}")


