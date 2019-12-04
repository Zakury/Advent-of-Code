# Secure Container
# Part 2: Rank 15900

import re

with open("input") as input_file:
    lower, upper = map(int, input_file.read().split("-"))
    total = 0

    for password in range(lower, upper + 1):
        password = str(password)

        if list(password) == sorted(password):
            groups = [[password[0], 1]]

            for i, digit in enumerate(password[1:]):
                if groups[-1][0] == digit:
                    groups[-1][1] += 1
                else:
                    groups.append([digit, 1])

            if any(group[1] == 2 for group in groups):
                total += 1

    print(total)