# Secure Container
# Part 1: Rank 12804

import re

with open("input") as input_file:
    lower, upper = map(int, input_file.read().split("-"))
    valid = 0
    for password in range(lower, upper + 1):
        password = str(password)

        if list(password) == list(sorted(list(password))):
            if len(re.findall(r"([0-9])\1", password)) > 0:
                valid += 1

    print(valid)