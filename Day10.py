def read_input(input: str):
    with open(input) as f:
        lines = f.read().splitlines()
    return lines


def execute_program(input: list, x: int, register: list):
    cycle = 0
    register[cycle] = x

    for row in input:
        if row == "noop":
            # 1
            register[cycle] = x
            cycle += 1
            continue
        else:
            command = row.split(" ")
        if command[0] == "addx":
            # 2
            register[cycle] = x
            cycle += 1
            # 3
            register[cycle] = x
            cycle += 1
            # 4
            x += int(command[1])
            register[cycle] = x

    return register


def calculate_signal_strength(register: list, cycles: list):
    strength = 0

    for i in cycles:
        strength += register[i - 1] * i

    return strength


def draw_CRT(register: list, crt_cycles: int):
    crt = [" "] * crt_cycles

    for cycle in range(len(crt)):
        if register[cycle] == (cycle - 1) % 40 \
                or register[cycle] == cycle % 40 \
                or register[cycle] == (cycle + 1) % 40:
            crt[cycle] = "#"

    for i in range(6):
        line = ""
        for j in range(i * 40, (i + 1) * 40):
            line += (str(crt[j]))
        print(line)

    return crt


if __name__ == '__main__':
    input = read_input("input10")
    crt_cycles = 240
    reg_x = [0] * crt_cycles
    x = 1
    register = execute_program(input, x, reg_x)
    cycles = [20, 60, 100, 140, 180, 220]
    # print(register)

    print(calculate_signal_strength(register, cycles))

    draw_CRT(register, crt_cycles)
