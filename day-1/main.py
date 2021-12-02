import os.path


def part_one(file):
    file.seek(0)
    lines_in_file = file.readlines()
    num_increased = 0
    data = []

    for line in lines_in_file:
        data.append(int(line))

    for idx, item in enumerate(data):
        if idx == 0:
            continue
        if data[idx] > data[idx - 1]:
            num_increased += 1

    print(f"part one: {num_increased}\n")


def part_two(file):
    file.seek(0)
    lines_in_file = file.readlines()
    num_increased = 0
    data = []

    for line in lines_in_file:
        data.append(int(line))

    sliding_window_sums = []
    for idx, item in enumerate(data):
        sliding_window = 3
        sum_current = 0

        for x in range(sliding_window):
            if idx+x < len(data):
                sum_current += data[idx+x]

        sliding_window_sums.append(sum_current)

    for idx, item in enumerate(sliding_window_sums):
        if idx == 0:
            continue
        if sliding_window_sums[idx] > sliding_window_sums[idx - 1]:
            num_increased += 1

    print(f"part two: {num_increased}")


def main():
    try:
        with open(os.path.join(os.path.dirname(__file__), "report.txt"), "r") as file:
            part_one(file)
            part_two(file)
    except IOError:
        print("File not found...")


if __name__ == '__main__':
    main()
