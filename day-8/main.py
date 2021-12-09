import os.path

displays = []


class Display:
    part_one_count = 0
    display_input = []
    display_output = []
    signal_map = []
    zero_six_nine = []
    two_three_five = []

    def __init__(self, display_input, display_output):
        self.display_input = display_input
        self.display_output = display_output
        self.signal_map = [set(), set(), set(), set(), set(), set(), set(), set(), set(), set()]
        self.zero_six_nine = [set(), set(), set()]
        self.two_three_five = [set(), set(), set()]
        self.part_one_count = self.part_one()
        self.map_1478()
        self.map_069()
        self.map_235()

    def part_one(self):
        count = 0
        for value in self.display_output:
            if len(value) == 2:
                count += 1
            elif len(value) == 3:
                count += 1
            elif len(value) == 4:
                count += 1
            elif len(value) == 7:
                count += 1
        return count

    def map_1478(self):
        for value in self.display_input:
            if len(value) == 2:
                self.signal_map[1] = value
            elif len(value) == 3:
                self.signal_map[7] = value
            elif len(value) == 4:
                self.signal_map[4] = value
            elif len(value) == 7:
                self.signal_map[8] = value

    def map_235(self):
        for value in self.display_input:
            if len(value) == 5:
                self.two_three_five.append(value)
        for value in self.two_three_five:
            if len(value - self.signal_map[1]) == 3:
                self.signal_map[3] = value
            elif len(value - self.signal_map[6]) == 0:
                self.signal_map[5] = value
            else:
                self.signal_map[2] = value

    def map_069(self):
        for value in self.display_input:
            if len(value) == 6:
                self.zero_six_nine.append(value)

        for value in self.zero_six_nine:
            if len(value - (self.signal_map[8] - self.signal_map[1])) == 1:
                self.signal_map[6] = value
            elif len(value - self.signal_map[4]) == 3:
                self.signal_map[0] = value
            else:
                self.signal_map[9] = value

    def construct_output(self):
        output = ""
        for value in self.display_output:
            for idx, signal_input in enumerate(self.signal_map):
                if value == signal_input:
                    output += str(idx)
        return int(output)


def load_data(file):

    for line in file:
        input_sets = []
        output_sets = []
        display_input = line.split(" | ")[0].split(" ")
        display_output = line.split(" | ")[1].strip().split(" ")

        for value in display_input:
            input_sets.append(set([char for char in value]))
        for value in display_output:
            output_sets.append(set([char for char in value]))

        displays.append(Display(input_sets, output_sets))


def main():
    try:
        with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
            load_data(file)

            input_sum = 0
            for display in displays:
                input_sum += display.part_one_count
            print(f"part one: {input_sum}")

            output_sum = 0
            for display in displays:
                output_sum += display.construct_output()
            print(f"Sum of display outputs: {output_sum}")

    except IOError:
        print("File not found...")


if __name__ == "__main__":
    main()
