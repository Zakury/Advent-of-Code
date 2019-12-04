# The Tyranny of the Rocket Equation
# Part 2: Rank 681

with open("input") as input_file:
    masses = map(int, input_file.readlines())
    total = 0

    for mass in masses:
        fuel = int(mass / 3) - 2
        total += fuel

        while fuel > 0:
            fuel = int(fuel / 3) - 2
            if fuel > 0:
                total += fuel

print(total)