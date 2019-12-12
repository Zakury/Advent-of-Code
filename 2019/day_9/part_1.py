# Sensor Boost
# Part 1: Rank 13914

with open("input") as input_file:
    intcodes = { int(index): int(value) for index, value in enumerate(input_file.read().split(",")) }
    location = 0
    relative = 0

    def mget(index, mode = 0):
        if mode == 0:
            return intcodes.get(mget(index, 1), 0)
        if mode == 1:
            return intcodes.get(index, 0)
        if mode == 2:
            return intcodes.get(mget(index, 1) + relative, 0)

    def mset(index, value, mode = 0):
        if mode == 0:
            intcodes[index] = value
        if mode == 2:
            intcodes[index + relative] = value

    while location < max(intcodes.keys()):
        if location in intcodes:
            parameter = str(mget(location, 1))[:-2].zfill(3)
            operation = str(mget(location, 1))[-2:].zfill(2)

            mode_1, mode_2, mode_3 = map(int, reversed(parameter))
        else:
            location += 1
            continue

        if operation == "01":
            mset(mget(location + 3, 1), mget(location + 1, mode_1) + mget(location + 2, mode_2), mode_3)
            location += 4
        if operation == "02":
            mset(mget(location + 3, 1), mget(location + 1, mode_1) * mget(location + 2, mode_2), mode_3)
            location += 4
        if operation == "03":
            mset(mget(location + 1, 1), int(input("IN: ")), mode_1)
            location += 2
        if operation == "04":
            print(mget(location + 1, mode_1))
            location += 2
        if operation == "05":
            if not mget(location + 1, mode_1) == 0:
                location = mget(location + 2, mode_2)
            else:
                location += 3
        if operation == "06":
            if mget(location + 1, mode_1) == 0:
                location = mget(location + 2, mode_2)
            else:
                location += 3
        if operation == "07":
            mset(mget(location + 3, 1), int(mget(location + 1, mode_1) < mget(location + 2, mode_2)), mode_3)
            location += 4
        if operation == "08":
            mset(mget(location + 3, 1), int(mget(location + 1, mode_1) == mget(location + 2, mode_2)), mode_3)
            location += 4
        if operation == "09":
            relative += mget(location + 1, mode_1)
            location += 2
        if operation == "99":
            break