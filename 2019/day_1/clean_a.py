# The Tyranny of the Rocket Equation
# Part 1: Clean Version

total_fuel = 0

with open("input_a.txt") as input_a:
    for mass in input_a.readlines():
        total_fuel += int(mass) // 3 - 2

print(total_fuel)