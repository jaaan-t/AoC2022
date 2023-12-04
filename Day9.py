def read_input(input: str):
    with open(input) as f:
        lines = f.read().splitlines()
    return lines


def write_output(file: str, matrix: list):
    f = open(file, "w")
    for row in matrix:
        rowStr = ""
        for col in row:
            rowStr += col
        f.write(rowStr + "\n")
    f.close()


def make_matrix(rows: int, cols: int):
    matrix = []

    for i in range(rows):
        matrix.append(["_"] * cols)

    return matrix


def clear_matrix(matrix: list):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = "_"


def print_matrix(matrix: list):
    for row in matrix:
        rowStr = ""
        for col in row:
            rowStr += col
        print(rowStr)


def follow_instructions_1(input: list, main_matrix: list, path_of_T: list, start: tuple):
    head = [start[0], start[1]]
    tail = [start[0], start[1]]
    main_matrix[head[0]][head[1]] = "H"
    path_of_T[tail[0]][tail[1]] = "T"

    for line in input:
        move = line.split(" ")
        dir = move[0]
        steps = int(move[1])
        for i in range(steps):
            if dir == "D":
                head[0] += 1
            elif dir == "U":
                head[0] -= 1
            elif dir == "L":
                head[1] -= 1
            elif dir == "R":
                head[1] += 1
            tail = move_knot(head, tail)
            main_matrix[head[0]][head[1]] = "H"
            main_matrix[tail[0]][tail[1]] = "T"
            path_of_T[tail[0]][tail[1]] = "T"
            # print_matrix(main_matrix)
            # print()


def follow_instructions_2(input: list, main_matrix: list, path_of_T: list, start: tuple):
    head = [start[0], start[1]]
    knot1 = [start[0], start[1]]
    knot2 = [start[0], start[1]]
    knot3 = [start[0], start[1]]
    knot4 = [start[0], start[1]]
    knot5 = [start[0], start[1]]
    knot6 = [start[0], start[1]]
    knot7 = [start[0], start[1]]
    knot8 = [start[0], start[1]]
    tail = [start[0], start[1]]

    main_matrix[head[0]][head[1]] = "H"
    path_of_T[tail[0]][tail[1]] = "T"

    for line in input:
        move = line.split(" ")
        dir = move[0]
        steps = int(move[1])
        # print(dir, steps)
        for i in range(steps):
            # clear_matrix(main_matrix)
            if dir == "D":
                head[0] += 1
            elif dir == "U":
                head[0] -= 1
            elif dir == "L":
                head[1] -= 1
            elif dir == "R":
                head[1] += 1
            main_matrix[head[0]][head[1]] = "H"
            knot1 = move_knot(head, knot1)
            main_matrix[knot1[0]][knot1[1]] = "1"
            knot2 = move_knot(knot1, knot2)
            main_matrix[knot2[0]][knot2[1]] = "2"
            knot3 = move_knot(knot2, knot3)
            main_matrix[knot3[0]][knot3[1]] = "3"
            knot4 = move_knot(knot3, knot4)
            main_matrix[knot4[0]][knot4[1]] = "4"
            knot5 = move_knot(knot4, knot5)
            main_matrix[knot5[0]][knot5[1]] = "5"
            knot6 = move_knot(knot5, knot6)
            main_matrix[knot6[0]][knot6[1]] = "6"
            knot7 = move_knot(knot6, knot7)
            main_matrix[knot7[0]][knot7[1]] = "7"
            knot8 = move_knot(knot7, knot8)
            main_matrix[knot8[0]][knot8[1]] = "8"
            tail = move_knot(knot8, tail)
            main_matrix[tail[0]][tail[1]] = "T"
            path_of_T[tail[0]][tail[1]] = "T"
            # print_matrix(main_matrix)
            # print()


def move_knot(head: list, knot: list):
    # H__
    # __T
    # H__
    if head[1] == knot[1] - 2 and head[0] != knot[0]:
        knot[1] -= 1
        if head[0] > knot[0]:
            knot[0] += 1
        else:
            knot[0] -= 1

    # __H
    # T__
    # __H
    elif head[1] == knot[1] + 2 and head[0] != knot[0]:
        knot[1] += 1
        if head[0] > knot[0]:
            knot[0] += 1
        else:
            knot[0] -= 1

    # _T_
    # ___
    # H_H
    elif head[0] == knot[0] + 2 and head[1] != knot[1]:
        knot[0] += 1
        if head[1] > knot[1]:
            knot[1] += 1
        else:
            knot[1] -= 1

    # H_H
    # ___
    # _T_
    elif head[0] == knot[0] - 2 and head[1] != knot[1]:
        knot[0] -= 1
        if head[1] > knot[1]:
            knot[1] += 1
        else:
            knot[1] -= 1

    # T
    # _
    # H
    elif head[1] == knot[1] + 2:
        knot[1] += 1

    # H
    # _
    # T
    elif head[1] == knot[1] - 2:
        knot[1] -= 1

    # T_H
    elif head[0] == knot[0] + 2:
        knot[0] += 1

    # H_T
    elif head[0] == knot[0] - 2:
        knot[0] -= 1

    return knot


def count_tail_moves(path_of_t: list):
    count = 0
    for row in path_of_t:
        for col in row:
            if col == "T":
                count += 1
    return count


if __name__ == '__main__':
    input = read_input("input9")
    main_matrix = make_matrix(10000, 1000)
    path_of_T = make_matrix(1000, 10000)
    start = 500, 500
    follow_instructions_1(input, main_matrix, path_of_T, start)
    # print()
    # print_matrix(main_matrix)
    # print()
    # print_matrix(path_of_T)
    print(count_tail_moves(path_of_T))

    # i = 21
    # j = 27
    i = 1000
    j = 1000
    # start2 = 15, 11
    start2 = i // 2, j // 2
    main_matrix2 = make_matrix(i, j)
    path_of_T2 = make_matrix(i, j)
    follow_instructions_2(input, main_matrix2, path_of_T2, start2)
    # print()
    # print_matrix(main_matrix2)
    # print()
    # print_matrix(path_of_T2)
    print(count_tail_moves(path_of_T2))
    # write_output("output9.txt", main_matrix2)
