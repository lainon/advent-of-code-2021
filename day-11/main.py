import inspect
import os.path


def load_data(file):
    file.seek(0)
    grid = []
    for line in file:
        grid.append([[int(char), False] for char in line.strip()])
    return grid


def part_one(file):
    grid = load_data(file)
    flash_total = step(grid, 100, 0, None, 1)
    print(f"part one: {flash_total}")


def part_two(file):
    grid = load_data(file)
    iteration = step(grid, 2 ^ 32, 0, None, 1)
    print(f"part two: {iteration}")


def step(grid, num_steps, num_flashes, calling_function, iteration):
    if calling_function is None:
        calling_function = inspect.stack()[1].function

    for x, row in enumerate(grid):
        for y, element in enumerate(row):
            grid[x][y][1] = False
            grid[x][y][0] += 1
            if grid[x][y][0] > 9:
                grid[x][y][1] = True

    flashy_octopus_positions = set(get_flashed(grid))

    while len(flashy_octopus_positions) > 0:
        flashy_octopus = list(flashy_octopus_positions)[0]
        vertical_octopus_positions = get_vertical(flashy_octopus, grid)
        horizontal_octopus_positions = get_horizontal(flashy_octopus, grid)
        diagonal_octopus_positions = get_diagonal(flashy_octopus, grid)

        for vertical_octopus in vertical_octopus_positions:
            x = vertical_octopus[0]
            y = vertical_octopus[1]
            grid[x][y][0] += 1
            if grid[x][y][0] > 9 and not grid[x][y][1]:
                grid[x][y][1] = True
                flashy_octopus_positions.add(vertical_octopus)
        for horizontal_octopus in horizontal_octopus_positions:
            x = horizontal_octopus[0]
            y = horizontal_octopus[1]
            grid[x][y][0] += 1
            if grid[x][y][0] > 9 and not grid[x][y][1]:
                grid[x][y][1] = True
                flashy_octopus_positions.add(horizontal_octopus)
        for diagonal_octopus in diagonal_octopus_positions:
            x = diagonal_octopus[0]
            y = diagonal_octopus[1]
            grid[x][y][0] += 1
            if grid[x][y][0] > 9 and not grid[x][y][1]:
                grid[x][y][1] = True
                flashy_octopus_positions.add(diagonal_octopus)
        flashy_octopus_positions.remove(flashy_octopus)

    final_flashy_octopus_positions = get_flashed(grid)
    final_flashy_octopus_total = num_flashes
    for flashy_octopus in final_flashy_octopus_positions:
        x = flashy_octopus[0]
        y = flashy_octopus[1]
        grid[x][y][0] = 0
        final_flashy_octopus_total += 1

    if calling_function == 'part_two':
        if synchronized(grid):
            return iteration
        else:
            return step(grid, num_steps - 1, final_flashy_octopus_total, calling_function, iteration + 1)

    elif calling_function == 'part_one':
        if num_steps > 1:
            return step(grid, num_steps - 1, final_flashy_octopus_total, calling_function, iteration + 1)
        else:
            return final_flashy_octopus_total


def synchronized(grid):
    for row in grid:
        for element in row:
            if not element[1]:
                return False
    return True


def get_flashed(grid):
    flashed = []
    for x, row in enumerate(grid):
        for y, element in enumerate(row):
            if element[0] > 9:
                flashed.append((x, y))
    return flashed


def get_vertical(position, grid):
    vertical = []
    if not is_top(position) and not grid[position[0] - 1][position[1]][1]:
        vertical.append((position[0] - 1, position[1]))
    if not is_bottom(position, grid) and not grid[position[0] + 1][position[1]][1]:
        vertical.append((position[0] + 1, position[1]))
    return vertical


def get_horizontal(position, grid):
    horizontal = []
    if not is_left(position) and not grid[position[0]][position[1] - 1][1]:
        horizontal.append((position[0], position[1] - 1))
    if not is_right(position, grid) and not grid[position[0]][position[1] + 1][1]:
        horizontal.append((position[0], position[1] + 1))
    return horizontal


def get_diagonal(position, grid):
    diagonal = []
    if not is_left(position):
        if not is_top(position) and not grid[position[0] - 1][position[1] - 1][1]:
            diagonal.append((position[0] - 1, position[1] - 1))
        if not is_bottom(position, grid) and not grid[position[0] + 1][position[1] - 1][1]:
            diagonal.append((position[0] + 1, position[1] - 1))
    if not is_right(position, grid):
        if not is_top(position) and not grid[position[0] - 1][position[1] + 1][1]:
            diagonal.append((position[0] - 1, position[1] + 1))
        if not is_bottom(position, grid) and not grid[position[0] + 1][position[1] + 1][1]:
            diagonal.append((position[0] + 1, position[1] + 1))
    return diagonal


def is_top(position):
    if position[0] == 0:
        return True
    return False


def is_bottom(position, grid):
    if position[0] == len(grid) - 1:
        return True
    return False


def is_left(position):
    if position[1] == 0:
        return True
    return False


def is_right(position, grid):
    if position[1] == len(grid[position[0]]) - 1:
        return True
    return False


def main():
    try:
        with open(os.path.join(os.path.dirname(__file__), "input2.txt"), "r") as file:
            part_one(file)
            part_two(file)

    except IOError:
        print("File not found...")


if __name__ == "__main__":
    main()
