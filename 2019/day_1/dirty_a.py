# The Tyranny of the Rocket Equation
# Part 1: Rank 291

with open("input_a.txt") as input_a:
    masses = map(int, input_a.readlines())
    total = 0

    for mass in masses:
        total += int(mass / 3) - 2

print(total)