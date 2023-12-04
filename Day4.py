def readInput(input: str):
    with open(input) as f:
        lines = f.read().split("\n")
    return lines


def makePair(line: str):
    pair = line.split(",")
    x1, x2 = pair[0].split("-")
    y1, y2 = pair[1].split("-")
    x1, x2 = int(x1), int(x2)
    y1, y2 = int(y1), int(y2)
    return x1, x2, y1, y2


def findFullyContained(pair):
    x1, x2, y1, y2 = pair[0:4]

    if x1 >= y1 and x2 <= y2:
        return 1

    # elif would be wrong!
    if x1 <= y1 and x2 >= y2:
        return 1

    return 0


def findOverlap(pair):
    x1, x2, y1, y2 = pair[0:4]

    if y1 <= x1 <= y2:
        return 1
    if x1 <= y1 <= x2:
        return 1

    return 0


if __name__ == '__main__':
    lines = readInput("input4")

    count = 0
    for line in lines:
        pair = findFullyContained(makePair(line))
        count += pair
    print("fully: ", count)

    count = 0
    for line in lines:
        pair = findOverlap(makePair(line))
        count += pair
    print("overlap: ", count)
