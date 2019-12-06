# Universal Orbit Map
# Part 1: Rank 11682

with open("input") as input_file:
    total = 0
    orbits = { 
        orbit.split(")")[1]: orbit.split(")")[0] 
        for orbit in input_file.read().split("\n") 
    }

    for key in orbits.keys():
        while True:
            try:
                key = orbits[key]
                total += 1
            except:
                break

    print(total)