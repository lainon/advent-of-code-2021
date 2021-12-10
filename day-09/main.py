from enum import Enum
import os.path

height_map = []
minimums = []
basins = []


class FromDirection(Enum):
    NONE = -1
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3


class Basin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.values = []
        self.visited = []
        self.downward_flow(self.x, self.y, self.values, FromDirection.NONE)

    def size(self):
        return len(self.values)

    def downward_flow(self, x, y, values, from_direction):
        if [x, y] in self.visited:
            return
        else:
            self.values.append(height_map[x][y])
            self.visited.append([x, y])

        current = height_map[x][y]
        up = down = left = right = -1
        if not is_top(x):
            up = height_map[x-1][y]
        if not is_bottom(x):
            down = height_map[x+1][y]
        if not is_left(y):
            left = height_map[x][y-1]
        if not is_right(x, y):
            right = height_map[x][y+1]

        if up != -1 and from_direction != FromDirection.UP:
            if 9 > up > current:
                self.downward_flow(x-1, y, values, FromDirection.DOWN)
        if down != -1 and from_direction != FromDirection.DOWN:
            if 9 > down > current:
                self.downward_flow(x+1, y, values, FromDirection.UP)
        if left != -1 and from_direction != FromDirection.LEFT:
            if 9 > left > current:
                self.downward_flow(x, y-1, values, FromDirection.RIGHT)
        if right != -1 and from_direction != FromDirection.RIGHT:
            if 9 > right > current:
                self.downward_flow(x, y+1, values, FromDirection.LEFT)


def is_top(x):
    return x == 0


def is_bottom(x):
    return x == len(height_map) - 1


def is_left(y):
    return y == 0


def is_right(x, y):
    return y == len(height_map[x]) - 1


def horizontal_minimum(x, y):
    if is_left(y):
        return height_map[x][y] < height_map[x][y+1]
    elif is_right(x, y):
        return height_map[x][y] < height_map[x][y-1]
    else:
        return height_map[x][y] < height_map[x][y+1] and height_map[x][y] < height_map[x][y-1]


def vertical_minimum(x, y):
    if is_top(x):
        return height_map[x][y] < height_map[x+1][y]
    elif is_bottom(x):
        return height_map[x][y] < height_map[x-1][y]
    else:
        return height_map[x][y] < height_map[x+1][y] and height_map[x][y] < height_map[x-1][y]


def risk_level():
    sums_plus_one = 0
    for value in minimums:
        sums_plus_one += value + 1
    return sums_plus_one


def load_data(file):
    file.seek(0)
    for line in file:
        height_map.append([int(value) for value in line.strip()])


def main():
    try:
        with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
            load_data(file)
            for x, row in enumerate(height_map):
                for y, value in enumerate(row):
                    if horizontal_minimum(x, y) and vertical_minimum(x, y):
                        basins.append(Basin(x, y))
                        minimums.append(value)
            print(f"part one: {risk_level()}")

            basin_mult = 1
            basins.sort(key=lambda l: l.size(), reverse=True)
            for i in range(3):
                basin_mult *= basins[i].size()
            print(f"part two: {basin_mult}")

    except IOError:
        print("File not found...")


if __name__ == "__main__":
    main()
