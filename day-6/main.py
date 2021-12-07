from collections import deque
import os.path


def cycle(iterations, lanternfishies):
    lanternfishies.rotate(-1)
    lanternfishies[5] += lanternfishies[7]

    if iterations == 0:
        fishy_sum = 0
        for fishy in lanternfishies:
            fishy_sum += fishy
        print(f"Number of fishies: {fishy_sum}")
        return

    cycle(iterations - 1, lanternfishies)


def load_data(file):
    lanternfishies = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for value in [int(i) for i in file.readline().split(",")]:
        lanternfishies[value] += 1
    return deque(lanternfishies)


def main():
    try:
        with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
            cycle(256, load_data(file))
    except IOError:
        print("File not found...")


if __name__ == "__main__":
    main()
