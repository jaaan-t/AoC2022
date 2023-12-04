def read(input: str):
    with open(input) as f:
        return f.read()


def compare_packets(left, right):
    if type(left) == int and type(right) == int:
        if left < right:
            return 1  # right order
        elif left > right:
            return -1  # wrong order
        else:
            return 0  # same value, continue

    elif type(left) == list and type(right) == list:
        if len(left) == len(right):
            for i in range(len(left)):
                sum = compare_packets(left[i], right[i])
                if sum == 1:
                    return 1
                if sum == -1:
                    return -1
        elif len(left) < len(right):
            for i in range(len(left)):
                sum = compare_packets(left[i], right[i])
                if sum == 1:
                    return 1
                if sum == -1:
                    return -1
            return 1  # left side ran out, right order
        else:
            for i in range(len(right)):
                sum = compare_packets(left[i], right[i])
                if sum == 1:
                    return 1
                if sum == -1:
                    return -1
            return -1  # right side ran out, wrong order

    elif type(left) == list and type(right) == int:
        return compare_packets(left, [right])

    elif type(left) == int and type(right) == list:
        return compare_packets([left], right)


if __name__ == '__main__':
    file = "input13"
    input = read(file).strip().split("\n\n")
    pairs = []
    for line in input:
        pairs.append((eval(line.split("\n")[0]), eval(line.split("\n")[1])))
    sum = 0
    for i in range(len(pairs)):
        if compare_packets(pairs[i][0], pairs[i][1]) == 1:
            sum += i + 1
    print(sum)

    input2 = read(file).strip().split("\n")
    packets = []
    for line in input2:
        if line != "":
            packets.append(eval(line))
    packets.append([[2]])
    packets.append([[6]])
    for i in range(len(packets)):
        for j in range(len(packets) - 1):
            if compare_packets(packets[j], packets[j + 1]) == -1:
                temp = packets[j]
                packets[j] = packets[j + 1]
                packets[j + 1] = temp
    print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
