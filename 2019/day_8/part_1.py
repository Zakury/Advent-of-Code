# Space Image Format
# Part 1: Rank 1183

WIDE, TALL = 25, 6

with open("input") as input_file:
    input_data = input_file.read()
    img_layers = [input_data[i:i + WIDE * TALL] for i in range(0, len(input_data), WIDE * TALL)]

    img_layers.sort(key = lambda layer: layer.count("0"))

    print(img_layers[0].count("1") * img_layers[0].count("2"))