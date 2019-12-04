# The Tyranny of the Rocket Equation
# Part 1: Rank 291

with open("input") as input_file:
    masses = map(int, input_file.readlines())
    total = 0

    for mass in masses:
        total += int(mass / 3) - 2

print(total)