# The Tyranny of the Rocket Equation
# Part 2: Clean Version

total_fuel = 0

with open("input_b.txt") as input_b:
    for mass in input_b.readlines():
        fuel = int(mass) // 3 - 2

        while fuel > 0:
            total_fuel += fuel
            fuel = fuel // 3 - 2

print(total_fuel)