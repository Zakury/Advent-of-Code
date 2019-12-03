# The Tyranny of the Rocket Equation
# Part 1: Rank 291

with open("input_1.txt") as input_1:
    masses = map(int, input_1.readlines())
    total = 0

    for mass in masses:
        total += int(mass / 3) - 2

print(total)