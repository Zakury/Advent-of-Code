# 1202 Program Alarm
# Part 1: Rank 457

with open("input") as input_file:
    numbers = list(map(int, input_file.read().split(",")))
    
    position = 0

    numbers[1] = 12
    numbers[2] = 2

    while position < len(numbers):
        if numbers[position] == 1:
            numbers[numbers[position + 3]] = numbers[numbers[position + 1]] + numbers[numbers[position + 2]]
            position += 4

        if numbers[position] == 2:
            numbers[numbers[position + 3]] = numbers[numbers[position + 1]] * numbers[numbers[position + 2]]
            position += 4

        if numbers[position] == 99:
            print(numbers[0])
            break