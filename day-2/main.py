import inspect
import os.path

position = [0, 0, 0]


def load_data(file):
    data = []
    file.seek(0)
    lines_in_file = file.readlines()

    for line in lines_in_file:
        args = line.split(" ")
        data.append((args[0], int(args[1])))

    return data


def command(cmd, amt):
    calling_function = inspect.stack()[1].function

    match cmd:
        case "forward":
            if calling_function == "part_one":
                position[0] += amt
            elif calling_function == "part_two":
                position[0] += amt
                position[1] += amt*position[2]
        case "down":
            if calling_function == "part_one":
                position[1] += amt
            elif calling_function == "part_two":
                position[2] += amt
        case "up":
            if calling_function == "part_one":
                position[1] -= amt
            elif calling_function == "part_two":
                position[2] -= amt
        case _:
            print("Invalid command...")

    return position


def part_one(data):
    global position
    for tuple in data:
        command(tuple[0], tuple[1])

    print(f"part_one: {position[0]*position[1]}")
    position = [0, 0, 0]


def part_two(data):
    global position
    for tuple in data:
        command(tuple[0], tuple[1])

    print(f"part_two: {position[0]*position[1]}")
    position = [0, 0, 0]


def main():
    try:
        with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
            part_one(load_data(file))
            part_two(load_data(file))
    except IOError:
        print("File not found...")


if __name__ == '__main__':
    main()
