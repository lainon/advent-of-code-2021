import os.path


def load_data(file):
    file.seek(0)
    data = [i.strip() for i in file]
    number_of_bits = len(data[0])
    return data, number_of_bits


def part_one(loaded_data):
    data = loaded_data[0]
    number_of_bits = loaded_data[1]
    frequency = get_frequency(data, number_of_bits)
    g = get_gamma_rate(frequency, len(data))
    e = get_epsilon_rate(g)
    print(f"part_one: {int(g, 2) * int (e, 2)}")


def part_two(loaded_data):
    data = loaded_data[0]
    number_of_bits = loaded_data[1]
    o = get_o2_co2(data, number_of_bits, 0, True)
    c = get_o2_co2(data, number_of_bits, 0, False)
    print(f"part_two: {int(o, 2) * int (c, 2)}")


def get_frequency(data, number_of_bits):
    frequency = []
    for i in range(number_of_bits):
        frequency.append(0)
        for d in data:
            if d[i] == '1':
                frequency[i] += 1
    return frequency


def get_gamma_rate(frequency, data_length):
    g = ''
    for i in frequency:
        if i >= data_length/2:
            g += '1'
        else:
            g += '0'
    return g


def get_epsilon_rate(gamma_rate):
    invert_dict = {'0': '1', '1': '0'}
    e = ''
    for bit in gamma_rate:
        e += invert_dict[bit]
    return e


def get_o2_co2(data, number_of_bits, iteration, o2):
    pruned_data = []
    pruned_frequency = get_frequency(data, number_of_bits)

    if len(data) == 1:
        return data[0]

    else:
        g = get_gamma_rate(pruned_frequency, len(data))
        e = get_epsilon_rate(g)

        for d in data:
            if d[iteration] == g[iteration] and o2:
                pruned_data.append(d)
            if d[iteration] == e[iteration] and not o2:
                pruned_data.append(d)

        iteration += 1
        return get_o2_co2(pruned_data, number_of_bits, iteration, o2)


def main():
    try:
        with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
            part_one(load_data(file))
            part_two(load_data(file))
    except IOError:
        print("File not found...")


if __name__ == "__main__":
    main()
