# 1202 Program Alarm
# Part 2: Rank 239

for noun in range(0, 100):
    for verb in range(0, 100):
        with open("input_b.txt") as input_b:
            numbers = list(map(int, input_b.read().split(",")))
            
            position = 0

            numbers[1] = noun
            numbers[2] = verb

            while position < len(numbers):
                if numbers[position] == 1:
                    numbers[numbers[position + 3]] = numbers[numbers[position + 1]] + numbers[numbers[position + 2]]
                    position += 4

                if numbers[position] == 2:
                    numbers[numbers[position + 3]] = numbers[numbers[position + 1]] * numbers[numbers[position + 2]]
                    position += 4

                if numbers[position] == 99:
                    if numbers[0] == 19690720:
                        print(100 * noun + verb)
                    break