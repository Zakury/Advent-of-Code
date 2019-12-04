# Crossed Wires
# Part 2: Rank 1597

with open("input") as input_file:
    wire_1 = input_file.readline()[:-1].split(",")
    wire_2 = input_file.readline().split(",")
    distances = []
    positions = []
    totals = []
    x, y = 0, 0
    total = 0

    for i in wire_1:
        length = int(i[1:])

        for a in range(length):
            if i[0] == "U":
                y += 1
                total += 1
            if i[0] == "D":
                y -= 1
                total += 1
            if i[0] == "L":
                x -= 1
                total += 1
            if i[0] == "R":
                x += 1
                total += 1
            
            totals.append(total)
            positions.append((x, y))

    x, y = 0, 0
    total = 0
    for i in wire_2:
        length = int(i[1:])

        for a in range(length):
            if i[0] == "U":
                y += 1
                total += 1
            if i[0] == "D":
                y -= 1
                total += 1
            if i[0] == "L":
                x -= 1
                total += 1
            if i[0] == "R":
                x += 1
                total += 1
            
            if (x, y) in positions:
                distances.append(totals[positions.index((x, y))] + total)

    print(min(distances))