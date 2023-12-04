def print_grid(grid: list):
    line = ""
    for r in range(len(grid)):
        line += str(r).zfill(3) + " "
        for c in range(len(grid[r])):
            line += grid[r][c]
        line += "\n"
    print(line)


def find_dims(rocks: list):
    x_min = float('inf')
    x_max, y_max = 0, 0
    for i in range(len(rocks)):
        for j in range(len(rocks[i])):
            x_min = min(x_min, rocks[i][j][0])
            x_max = max(x_max, rocks[i][j][0])
            y_max = max(y_max, rocks[i][j][1])
    return x_min, x_max, y_max


def add_rocks(grid: list, rocks: list, offset: int):
    for i in range(len(rocks)):
        for j in range(len(rocks[i]) - 1):
            x_start = rocks[i][j][0] - x_min + offset
            y_start = rocks[i][j][1]
            x_end = rocks[i][j + 1][0] - x_min + offset
            y_end = rocks[i][j + 1][1]
            if x_start != x_end:
                for c in range(min(x_start, x_end), max(x_start, x_end) + 1):
                    grid[y_start][c] = "#"
            elif y_start != y_end:
                for r in range(min(y_start, y_end), max(y_start, y_end) + 1):
                    grid[r][x_start] = "#"


def add_sand_at_rest(grid: list, x_source: int, height: int, width: int):
    at_rest = True
    num_sand = 0
    while at_rest:
        if grid[0][x_source] == "o":
            break
        at_rest = False
        r, c = 0, x_source
        while not at_rest and r < height - 1 and c < width - 1:
            if grid[r + 1][c] == empty:
                r += 1
            elif grid[r + 1][c - 1] == empty:
                r += 1
                c -= 1
            elif grid[r + 1][c + 1] == empty:
                r += 1
                c += 1
            elif grid[r + 1][c] != empty and grid[r + 1][c - 1] != empty and grid[r + 1][c + 1] != empty:
                num_sand += 1
                grid[r][c] = "o"
                at_rest = True

    return num_sand


def add_never_ending_stream(grid: list, x_source: int, height: int, width: int):
    r, c = 0, x_source
    while r < height - 2:
        at_rest = False
        r, c = 0, x_source
        while not at_rest and r < height - 2 and c < width - 1:
            if grid[r + 1][c] == empty:
                r += 1
                grid[r][c] = "~"
            elif grid[r + 1][c - 1] == empty:
                r += 1
                c -= 1
                grid[r][c] = "~"
            elif grid[r + 1][c + 1] == empty:
                r += 1
                c += 1
                grid[r][c] = "~"
            elif grid[r + 1][c] != empty and grid[r + 1][c - 1] != empty and grid[r + 1][c + 1] != empty:
                grid[r][c] = "~"
                at_rest = True


def add_floor(grid: list):
    y = len(grid) - 1
    for c in range(len(grid[y])):
        grid[y][c] = "#"


def get_input(day: int, test: int):
    file = "input"
    if test:
        file = "test"
    with open(file + str(day)) as f:
        return f.read().strip().split("\n")


if __name__ == '__main__':
    ###############################
    DAY = 14
    TEST = 0
    INPUT = get_input(DAY, TEST)
    ###############################

    rocks = []
    for line in INPUT:
        rocks.append([tuple(map(int, x.split(","))) for x in line.split(" -> ")])
    x_min, x_max, y_max = find_dims(rocks)
    empty = "."

    # Part 1
    width = x_max - x_min + 1
    height = y_max + 1
    # print("x", width, "| y", height)
    grid = []
    for i in range(height):
        grid.append([empty] * width)
    x_source = 500 - x_min
    grid[0][x_source] = "+"
    add_rocks(grid, rocks, 0)
    num_sand = add_sand_at_rest(grid, x_source, height, width)
    add_never_ending_stream(grid, x_source, height, width)
    print_grid(grid)
    print(num_sand)

    # Part 2
    width = (x_max - x_min + 1) * 6
    height = y_max + 3
    # print("x", width, "| y", height)
    grid = []
    for i in range(height):
        grid.append([empty] * width)
    x_source = width // 2
    grid[0][x_source] = "+"
    add_rocks(grid, rocks, x_source - (500 - x_min))
    add_floor(grid)
    num_sand = add_sand_at_rest(grid, x_source, height, width)
    # print_grid(grid)
    print(num_sand)
