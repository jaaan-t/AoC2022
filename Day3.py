with open('input3') as f:
    lines = f.read().split("\n")


# a-z: 1-26
# A_Z: 27-52
def findPriorities(line: str) -> int:
    length = len(line)
    half1 = line[slice(0, length // 2)]
    half2 = line[slice(length // 2, length)]
    twice = 0
    for c in half1:
        if c in half2:
            twice = ord(c)
    if twice < 97:
        twice -= 38
    else:
        twice -= 96
    return twice


sumTotal = 0
for line in lines:
    sumTotal += findPriorities(line)
print(sumTotal)


def findBadges(a: str, b: str, c: str) -> int:
    badge = 0
    for letter in a:
        if letter in b and letter in c:
            badge = ord(letter)
    if badge < 97:
        badge -= 38
    else:
        badge -= 96
    return badge


badgeTotal = 0
for i in range(0, len(lines), 3):
    badgeTotal += findBadges(lines[i], lines[i + 1], lines[i + 2])
print(badgeTotal)
