def read_input(input: str):
    with open(input) as f:
        lines = f.read().splitlines()
    return lines


class Node:
    def __init__(self, elevation: int, i: int, j: int, start: bool, goal: bool):
        self.elevation = elevation
        self.i = i
        self.j = j
        self.neighbours = []
        self.start = start
        self.goal = goal
        self.marked = False
        self.parent = None

    def __str__(self):
        start = ""
        goal = ""
        marked = ""
        if self.start:
            start = " | Start"
        if self.goal:
            goal = " | Goal"
        if self.marked:
            marked = " m"

        return str(self.elevation) + " (" + str(self.i) + "," + str(self.j) \
               + ") neighbours: " + str(self.neighbours) + marked + start + goal


def make_nodes(grid: list):
    nodes = []
    start = None
    goal = None

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S" or grid[i][j] == "E":
                if grid[i][j] == "S":
                    node = Node(0, i, j, True, False)
                    start = node
                    grid[node.i][node.j] = 'a'
                elif grid[i][j] == "E":
                    node = Node(25, i, j, False, True)
                    goal = node
                    grid[node.i][node.j] = 'z'
                elevation = ord(grid[i][j])
                add_neighbours(node, i, i - 1, j, elevation, grid)
                add_neighbours(node, i, i + 1, j, elevation, grid)
                add_neighbours(node, i, i, j - 1, elevation, grid)
                add_neighbours(node, i, i, j + 1, elevation, grid)
                nodes.append(node)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i, j) != (start.i, start.j) and (i, j) != (goal.i, goal.j):
                elevation = ord(grid[i][j])
                node = Node(elevation - 97, i, j, False, False)
                add_neighbours(node, i, i - 1, j, elevation, grid)
                add_neighbours(node, i, i + 1, j, elevation, grid)
                add_neighbours(node, i, i, j - 1, elevation, grid)
                add_neighbours(node, i, i, j + 1, elevation, grid)
                nodes.append(node)

    return nodes


def add_neighbours(node, i, row, col, elevation, grid):
    if 0 <= row < len(grid) and 0 <= col < len(grid[i]):
        if ord(grid[row][col]) <= elevation + 1:
            node.neighbours.append((row, col))


def make_notes_dict(nodes: list):
    nodes_dict = {}
    for node in nodes:
        nodes_dict[(node.i, node.j)] = node
    return nodes_dict


if __name__ == '__main__':
    input = read_input("input12")
    lengths = []
    for i in range(1):
        grid = [[*line] for line in input]

        nodes = make_nodes(grid)
        nodes_dict = make_notes_dict(nodes)

        for node in nodes:
            if node.start:
                start = node
            if node.goal:
                goal = node

        unvisited = [start]
        while unvisited:
            current = unvisited.pop(0)
            for neighbour in current.neighbours:
                node = nodes_dict[neighbour]
                if not node.marked:
                    node.marked = True
                    unvisited.append(node)
                    node.parent = current

        backtrack = []
        node = goal
        while node != start:
            backtrack.append(node)
            node = node.parent
        print(len(backtrack))
        # for node in backtrack:
        #     print(node.parent)

        backtrack = []
        node = goal
        while node.elevation != 0:
            backtrack.append(node)
            node = node.parent
        print(len(backtrack))
        # for node in backtrack:
        #     print(node.parent)
