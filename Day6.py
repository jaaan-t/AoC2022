def readInput(input: str):
    with open(input) as f:
        lines = f.read()
    return lines


def findMarker(data: str, j: int):
    i = 0
    spot = data[i:j]
    foundMarker = False
    while not foundMarker:
        foundMarker = True
        for c in spot:
            if spot.count(c) > 1:
                foundMarker = False
        i += 1
        j += 1
        spot = data[i:j]
    return j - 1


if __name__ == '__main__':
    input = readInput("input6")
    print(findMarker(input, 4))
    print(findMarker(input, 14))
