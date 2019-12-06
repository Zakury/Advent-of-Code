# Sunny with a Chance of Asteroids
# Part 1: Rank 15976

with open("input") as input_file:
    position = 0
    numbers = input_file.read().split(",")

    while position < len(numbers):
        number = numbers[position]
        opcode = int(number[-2:])

        m1 = int(number[-3]) if len(number) > 2 else None
        m2 = int(number[-4]) if len(number) > 3 else None
        m3 = int(number[-5]) if len(number) > 4 else None

        if opcode == 1:
            val_1 = int(numbers[position + 1] if m1 else numbers[int(numbers[position + 1])])
            val_2 = int(numbers[position + 2] if m2 else numbers[int(numbers[position + 2])])

            numbers[int(numbers[position + 3])] = str(val_1 + val_2)
            position += 4

        if opcode == 2:
            val_1 = int(numbers[position + 1] if m1 else numbers[int(numbers[position + 1])])
            val_2 = int(numbers[position + 2] if m2 else numbers[int(numbers[position + 2])])

            numbers[int(numbers[position + 3])] = str(val_1 * val_2)
            position += 4

        if opcode == 3:
            numbers[int(numbers[position + 1])] = input("Program Input: ")
            position += 2

        if opcode == 4:
            print(numbers[int(numbers[position + 1])])
            position += 2

        if opcode == 99:
            break