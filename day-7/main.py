import os.path


def get_minimal_cost_one(crab_submarines):
    cost = 0
    middle = crab_submarines[int(len(crab_submarines)/2)]
    for submarine in crab_submarines:
        cost += abs(middle - submarine)
    return cost


def get_minimal_cost_two(crab_submarines, head, previous_cost):
    costs = []
    for submarine in crab_submarines:
        cost = sum(range(abs(submarine - head) + 1))
        costs.append(cost)

    if sum(costs) < previous_cost:
        return get_minimal_cost_two(crab_submarines, head - 1, sum(costs))
    else:
        return previous_cost

# the mean minimizes cost function for part 2, actually (not my solution)
# https://math.stackexchange.com/questions/113270/the-median-minimizes-the-sum-of-absolute-deviations-the-ell-1-norm


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
            print(f"part two: {get_minimal_cost_two(crab_submarines, int(len(crab_submarines)/2), float('inf'))}")

    except IOError:
        print("File not found...")


if __name__ == "__main__":
    main()
