# Universal Orbit Map
# Part 2: Rank 12230

with open("input") as input_file:
    orbits = { 
        orbit.split(")")[1]: orbit.split(")")[0] 
        for orbit in input_file.read().split("\n") 
    }

    you = ["YOU", [], 0]
    san = ["SAN", [], 0]

    while True:
        if you[0] in orbits:
            you[1].append((you[0], you[2]))
            you[0] = orbits[you[0]]
            you[2] += 1

        if san[0] in orbits:
            san[1].append((san[0], san[2]))
            san[0] = orbits[san[0]]
            san[2] += 1

        if not san[0] in orbits and not you[0] in orbits:
            break

    points = set(point[0] for point in you[1]).intersection(
        set(point[0] for point in san[1])
    )

    distances = []

    for point in points:
        you_pos = list(filter(lambda part: part[0] == point, you[1]))[0]
        san_pos = list(filter(lambda part: part[0] == point, san[1]))[0]
        distances.append(you_pos[1] + san_pos[1])
    distances.sort()
    print(distances[0] - 2)