import functools
import operator
import os.path

lines = []
grid = [[0]*1000 for i in range(1000)]


class Line:
    b = 0
    slope = 0
    horizontal = False
    vertical = False
    points_on_line = []

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        self.set_slope()
        self.set_b()
        self.set_points_on_line()

    def set_slope(self):
        if self.point2[1] == self.point1[1]:
            self.horizontal = True

        elif self.point2[0] == self.point1[0]:
            self.vertical = True

        else:
            self.slope = (self.point2[1] - self.point1[1]) / (self.point2[0] - self.point1[0])

    def set_b(self):
        self.b = self.point1[1] - (self.point1[0] * self.slope)

    def set_points_on_line(self):
        self.points_on_line = []
        if self.horizontal:
            for x in range(min(self.point1[0], self.point2[0]), max(self.point1[0], self.point2[0]) + 1):
                self.points_on_line.append((self.point1[1], x))
        elif self.vertical:
            for y in range(min(self.point1[1], self.point2[1]), max(self.point1[1], self.point2[1]) + 1):
                self.points_on_line.append((y, self.point1[0]))
        else:
            for x in range(min(self.point1[0], self.point2[0]), max(self.point1[0], self.point2[0]) + 1):
                y = self.slope * x + self.b
                if y % 1 == 0:
                    self.points_on_line.append((int(y), x))


def find_overlaps():
    for line in lines:
        for point in line.points_on_line:
            grid[point[0]][point[1]] += 1

    sum_ge_2 = 0
    for row in grid:
        for element in row:
            if element > 1:
                sum_ge_2 += 1

    print(f"There are {sum_ge_2} overlaps of 2 or more lines.")


def load_data(file):
    global lines
    for line in file:
        points = tuple(map(int, (functools.reduce(operator.iconcat, [k for k in [j.split(",") for j in [i for i in line.strip().split(" -> ")]]], []))))
        lines.append(Line(points[0:2], points[2:4]))


def main():
    try:
        with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
            load_data(file)
            find_overlaps()
    except IOError:
        print("File not found...")


if __name__ == "__main__":
    main()
