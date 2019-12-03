# Crossed Wires
# Part 1: Rank 1850

with open("input_1.txt") as input_1:
    wire_1 = input_1.readline()[:-1].split(",")
    wire_2 = input_1.readline().split(",")
    distances = []
    positions = []
    x, y = 0, 0

    for i in wire_1:
        length = int(i[1:])

        for a in range(length):
            if i[0] == "U":
                y += 1
            if i[0] == "D":
                y -= 1
            if i[0] == "L":
                x -= 1
            if i[0] == "R":
                x += 1
            
            positions.append((x, y))

    x, y = 0, 0

    for i in wire_2:
        length = int(i[1:])

        for a in range(length):
            if i[0] == "U":
                y += 1
            if i[0] == "D":
                y -= 1
            if i[0] == "L":
                x -= 1
            if i[0] == "R":
                x += 1
            
            if (x, y) in positions:
                distances.append(abs(x) + abs(y))

    print(min(distances))