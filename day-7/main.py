import os.path


def get_minimal_cost_one(crab_submarines):
    cost = 0
    middle = crab_submarines[int(len(crab_submarines)/2)]
    for submarine in crab_submarines:
        cost += abs(middle - submarine)
    return cost


def get_minimal_cost_two(crab_submarines):
    costs = []
    for i in range(len(crab_submarines)):
        cost = 0
        for submarine in crab_submarines:
            cost += sum(range(abs(submarine - i) + 1))
        costs.append(cost)

    return sorted(costs)[0]


def load_data(file):
    file.seek(0)
    crab_submarines = []
    for submarine in [int(i) for i in file.readline().split(",")]:
        crab_submarines.append(submarine)
    return sorted(crab_submarines)


def main():
    try:
        with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
            crab_submarines = load_data(file)
            print(f"part one: {get_minimal_cost_one(crab_submarines)}")
            print(f"part two: {get_minimal_cost_two(crab_submarines)}")
    except IOError:
        print("File not found...")


if __name__ == "__main__":
    main()
