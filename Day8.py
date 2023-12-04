from time import perf_counter


def read_input(input: str):
    with open(input) as f:
        lines = f.read().split("\n")
    return lines


def calc_outside_num(input: list):
    length = len(input[0])
    height = len(input)
    return length * 2 + (height - 2) * 2


def produce_cols(input: list):
    cols = []

    for col in range(0, len(input[0])):
        colStr = ""
        for row in input:
            colStr += row[col]
        cols.append(colStr)

    return cols


def calc_visible_trees_in_rows(row: str):
    index = [0] * len(row)
    left_end = int(row[0])
    right_end = int(row[-1])
    max_from_left = left_end
    max_from_right = right_end

    for i in range(1, len(row) - 1):
        tree = int(row[i])
        if tree > left_end and tree > max_from_left:
            max_from_left = tree
            index[i] = 1

    for i in range(len(row) - 2, 0, -1):
        tree = int(row[i])
        if tree > right_end and tree > max_from_right:
            max_from_right = tree
            index[i] = 1

    return index


def make_matrix(input: list):
    # create empty matrix of size input
    matrix = []

    for i in range(len(input)):
        matrix.append([0] * len(input))

    return matrix


def calc_total_visible_trees(input: list):
    visible = calc_outside_num(input)

    visible_in_rows = []
    for row in range(1, len(input) - 1):
        visible_in_rows.append(calc_visible_trees_in_rows(input[row]))

    cols = produce_cols(input)
    visible_in_cols = []
    for col in range(1, len(cols) - 1):
        visible_in_cols.append(calc_visible_trees_in_rows(cols[col]))

    matrix = make_matrix(input)
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            if visible_in_rows[i - 1][j] == 1:
                matrix[i][j] = visible_in_rows[i - 1][j]

    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            if visible_in_cols[i - 1][j] == 1:
                matrix[j][i] = visible_in_cols[i - 1][j]

    for row in matrix:
        for col in row:
            visible += col

    return visible, matrix


def calc_scenic_score(input: list, row: int, col: int):
    score_left = 0
    score_right = 0
    score_up = 0
    score_down = 0
    tree = int(input[row][col])

    # look to the right
    for c in range(col + 1, len(input[row])):
        score_right += 1
        if int(input[row][c]) >= tree:
            break

    # look to the left
    for c in range(col - 1, -1, -1):
        score_left += 1
        if int(input[row][c]) >= tree:
            break

    # look down
    for r in range(row + 1, len(input)):
        score_down += 1
        if int(input[r][col]) >= tree:
            break

    # look up
    for r in range(row - 1, -1, -1):
        score_up += 1
        if int(input[r][col]) >= tree:
            break

    return score_left * score_right * score_up * score_down


def makes_scenic_score_matrix(input: list):
    matrix = make_matrix(input)

    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            matrix[i][j] = calc_scenic_score(input, i, j)

    return matrix


def find_biggest_element(matrix: list):
    max_element, row, col = 0, 0, 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if int(matrix[i][j]) > max_element:
                max_element = int(matrix[i][j])
                row, col = i, j

    return max_element, row, col


def find_hidden_tree_with_biggest_scenic_score(matrix_visible: list, matrix_scenic: list):
    tree, row, col = 0, 0, 0

    for i in range(len(matrix_scenic)):
        for j in range(len(matrix_scenic[i])):
            if int(matrix_scenic[i][j]) > tree and matrix_visible[i][j] == 0:
                tree = int(matrix_scenic[i][j])
                row, col = i, j

    return tree, row, col


if __name__ == '__main__':
    start = perf_counter()

    input = read_input("input8")
    total_visible, matrix_visible = calc_total_visible_trees(input)
    print("1)", total_visible)

    matrix_scenic = makes_scenic_score_matrix(input)
    scenic_score, i, j = (find_biggest_element(matrix_scenic))
    visible = matrix_visible[i][j]
    print("\n2) score:", scenic_score, "| height:", input[i][j], "| position:", i, j, "| visible:", visible)

    scenic_score, i, j = find_hidden_tree_with_biggest_scenic_score(matrix_visible, matrix_scenic)
    visible = matrix_visible[i][j]
    print("   score:", scenic_score, "| height:", input[i][j], "| position:", i, j, "| visible:", visible)

    stop = perf_counter()
    print("\nElapsed time:", round((stop - start) * 1e3, 2), "ms")
