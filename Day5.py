from collections import deque


def readInput(input: str):
    with open(input) as f:
        lines = f.read().split("\n")
    return lines


def parseInstructions(line: str):
    instruct = line.split(" ")
    return int(instruct[1]), int(instruct[3]) - 1, int(instruct[5]) - 1


def makeStacks(stacksRaw: list):
    stacksLists = []
    stacksStacks = []
    for line in stacksRaw:
        stacksLists.append([line[i + 1:i + 2] for i in range(0, len(line), 4)])
    for j in range(9):
        stack = deque()
        stacksStacks.append(stack)
        for i in range(len(stacksLists) - 1, -1, -1):
            stack.append(stacksLists[i][j])
    return stacksStacks


def cleanStack(stack: deque):
    popped = stack.pop()
    while popped == ' ':
        popped = stack.pop()
    if popped != ' ':
        stack.append(popped)


def moveCrates(numCrates: int, fromStack: deque, toStack: deque):
    for i in range(numCrates):
        toStack.append(fromStack.pop())


def moveCrates2(numCrates: int, fromStack: deque, toStack: deque):
    tempStack = deque()
    for i in range(numCrates):
        tempStack.append(fromStack.pop())
    for i in range(numCrates):
        toStack.append(tempStack.pop())


if __name__ == '__main__':
    instructions = readInput("input5_instructions")
    stacksRaw = readInput("input5_stacks")
    stacks = makeStacks(stacksRaw)
    for s in stacks:
        cleanStack(s)
    for line in instructions:
        move = parseInstructions(line)
        moveCrates(move[0], stacks[move[1]], stacks[move[2]])
    solution = ""
    for s in stacks:
        solution += s.pop()
    print("1:", solution)

    stacks = makeStacks(stacksRaw)
    for s in stacks:
        cleanStack(s)
    for line in instructions:
        move = parseInstructions(line)
        moveCrates2(move[0], stacks[move[1]], stacks[move[2]])
    solution = ""
    for s in stacks:
        solution += s.pop()
    print("2:", solution)
