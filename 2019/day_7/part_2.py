# Amplification Circuit
# Part 2: Rank 8462

class Amplifier:
    def __init__(self, phase):
        with open("input") as input_file:
            self.position = 0
            self.numbers = input_file.read().split(",")
            self.inputs = [phase]
            self.outputs = []

    def step(self):
        while True:
            number = self.numbers[self.position]
            opcode = int(number[-2:])

            m1 = int(number[-3]) if len(number) > 2 else None
            m2 = int(number[-4]) if len(number) > 3 else None
            m3 = int(number[-5]) if len(number) > 4 else None

            if opcode in [1, 2, 5, 6, 7, 8]:
                val_1 = int(self.numbers[self.position + 1] if m1 else self.numbers[int(self.numbers[self.position + 1])])
                val_2 = int(self.numbers[self.position + 2] if m2 else self.numbers[int(self.numbers[self.position + 2])])

            if opcode in [1, 2, 7, 8]:
                val_3 = int(self.numbers[self.position + 3])

            if opcode == 1:
                self.numbers[int(self.numbers[self.position + 3])] = str(val_1 + val_2)
                self.position += 4

            if opcode == 2:
                self.numbers[int(self.numbers[self.position + 3])] = str(val_1 * val_2)
                self.position += 4

            if opcode == 3:
                self.numbers[int(self.numbers[self.position + 1])] = self.inputs.pop(0)
                self.position += 2

            if opcode == 4:
                self.output.inputs.append(self.numbers[int(self.numbers[self.position + 1])])
                self.outputs.append(self.numbers[int(self.numbers[self.position + 1])])
                self.position += 2
                break

            if opcode == 5:
                if val_1 != 0:
                    self.position = val_2
                else:
                    self.position += 3

            if opcode == 6:
                if val_1 == 0:
                    self.position = val_2
                else:
                    self.position += 3

            if opcode == 7:
                self.numbers[val_3] = int(val_1 < val_2)
                self.position += 4

            if opcode == 8:
                self.numbers[val_3] = int(val_1 == val_2)
                self.position += 4

            if opcode == 99:
                return True

        return None

thrusters = []

for i in range(56789, 100000):
    signals = str(i)
    if len(signals) == 5 and set(sorted(signals)) == set(["5", "6", "7", "8", "9"]):
        amp_a = Amplifier(signals[0])
        amp_b = Amplifier(signals[1])
        amp_c = Amplifier(signals[2])
        amp_d = Amplifier(signals[3])
        amp_e = Amplifier(signals[4])

        amp_a.output = amp_b
        amp_b.output = amp_c
        amp_c.output = amp_d
        amp_d.output = amp_e
        amp_e.output = amp_a

        amp_a.inputs.append("0")

        output = False

        while not output:
            if any([
                amp_a.step(),
                amp_b.step(),
                amp_c.step(),
                amp_d.step(),
                amp_e.step()
            ]):
                thrusters.append(amp_e.outputs[-1])
                output = True

print(max(thrusters))