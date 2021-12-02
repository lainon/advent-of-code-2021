import operator
import os.path


def get_truth(a, relate, b):
    ops = {
        '>': operator.gt,
        '<': operator.lt,
        '>=': operator.ge,
        '<=': operator.le,
        '==': operator.eq,
        '!=': operator.ne
    }

    return ops[relate](a, b)


def load_data(file):
    file.seek(0)
    lines_in_file = file.readlines()
    data = []

    for line in lines_in_file:
        data.append(int(line))

    return data


def data_summation(data, window):
    sums = []

    for idx, d in enumerate(data):
        s = 0

        for x in range(window):
            if idx+x < len(data):
                s += data[idx+x]

        sums.append(s)

    return sums


def data_reduction(data, operation):
    result = 0

    for idx, item in enumerate(data):
        if idx == 0:
            continue
        if get_truth(data[idx], operation, data[idx-1]):
            result += 1

    return result


def part_one(data):
    print(f"part one: {data_reduction(data_summation(data, 1), '>')}")


def part_two(data):
    print(f"part two: {data_reduction(data_summation(data, 3), '>')}")


def main():
    try:
        with open(os.path.join(os.path.dirname(__file__), "report.txt"), "r") as file:
            part_one(load_data(file))
            part_two(load_data(file))
    except IOError:
        print("File not found...")


if __name__ == '__main__':
    main()
