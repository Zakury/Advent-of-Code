# Space Image Format
# Part 2: Rank 1353

WIDE, TALL = 25, 6

with open("input") as input_file:
    input_data = input_file.read()
    img_layers = [input_data[i:i + WIDE * TALL] for i in range(0, len(input_data), WIDE * TALL)]
    new_layers = []

    for layer in img_layers:
        new_layers.append([layer[i:i + WIDE] for i in range(0, len(layer), WIDE)])

    for y in range(TALL):
        for x in range(WIDE):
            final = "2"
            
            for layer in new_layers:
                color = layer[y][x]
                
                if color == "2":
                    if not final == "0" and not final == "1":
                        final = "2"
                        continue
                
                final = color
                break

            print("#" if final == "0" else " ", end = "")
        print()
