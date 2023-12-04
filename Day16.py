# class Node:
#     def __init__(self, ID: str, specs=None):
#         self.ID = ID
#         self.FLOW_RATE = specs[0] if specs is not None else 0
#         self.TUNNELS = specs[1] if specs is not None else []
#         self.neighbours = []
#         self.open = False
#         self.marked = False
#
#     def __str__(self):
#         open = "closed"
#         if self.open:
#             open = "open"
#         return self.ID + ": " + str(self.FLOW_RATE).zfill(2) + " " + str(self.TUNNELS) + " - " + str(open)
#
#
# def mark_node(node: Node):
#     node.marked = True

def dfs(nodes_tunnels: dict, current: str, visited: list, open: list, time_left: int, pressure: int):
    for node in open:
        pressure += nodes_flow[node]

    open_no_current = open.copy()

    if len(open) == to_open:
        time_left -= 1
        while time_left > 1:
            for node in open:
                pressure += nodes_flow[node]
            time_left -= 1
    else:
        visited.append(current)
        if nodes_flow[current] > 0 and current not in open:
            open.append(current)
            time_left -= 1

        for node in nodes_tunnels[current]:
            if time_left <= 1:
                break
            if len(visited) > 3 and (current, node) == (visited[-3], visited[-2]):
                break
            if len(visited) > 1 and len(visited) % 2 == 1:
                b = visited[:-1]
                c = b[:len(b) // 2]
                d = b[len(b) // 2:]
                if c == d:
                    break

            if len(paths) >= 5000:
                if pressure >= paths[-1][1] and pressure != paths[0][1]:
                    dfs(nodes_tunnels, node, visited.copy(), open.copy(), time_left - 1, pressure)
                    if len(open) != len(open_no_current):
                        dfs(nodes_tunnels, node, visited.copy(), open_no_current.copy(), time_left, pressure)
            else:
                dfs(nodes_tunnels, node, visited.copy(), open.copy(), time_left - 1, pressure)
                if len(open) != len(open_no_current):
                    dfs(nodes_tunnels, node, visited.copy(), open_no_current.copy(), time_left, pressure)

    visited_tuple = tuple(visited)
    if (visited_tuple, pressure) not in paths:
        paths.append((visited_tuple, pressure))
        paths.sort(key=lambda path: path[1], reverse=True)
        for i in range(10000, len(paths)):
            paths.pop()


def get_input(day: int, test: int):
    file = "input"
    if test:
        file = "test"
    with open(file + str(day)) as f:
        return f.read().strip().split("\n")


if __name__ == '__main__':
    ###############################
    DAY = 16
    TEST = 1
    INPUT = get_input(DAY, TEST)
    ###############################

    valves = {}
    for line in INPUT:
        s = line.split()
        valves[s[1]] = int(s[4].split("=")[1].split(";")[0]), [v.split(",")[0] for v in s[9:]]

    nodes_tunnels = {}
    nodes_flow = {}
    for valve in valves:
        nodes_tunnels[valve] = valves[valve][1]
        nodes_flow[valve] = valves[valve][0]
    for node in nodes_flow:
        if node != "AA" and not nodes_flow[node]:
            continue
        print(node, nodes_flow[node])

    # print(nodes_tunnels)
    # print(nodes_flow)
    # for node in nodes_tunnels:
    #     print(node, nodes_tunnels[node])
    # for node in nodes_flow:
    #     print(node, nodes_flow[node])

    # to_open = 0
    # for node in nodes_flow:
    #     if nodes_flow[node] > 0:
    #         to_open += 1
    #
    # opened_valves = []
    # visited_nodes = set()
    # paths = []
    # time = 30
    # dfs(nodes_tunnels, "AA", [], [], time + 1, 0)
    # print(paths)
    # print(len(paths))
    # max_pressure = 0
    # for path in paths:
    #     max_pressure = max(max_pressure, path[-1])
    #     if max_pressure == path[-1]:
    #         best_path = path
    # print(max_pressure)
    # print(best_path)
    # # nodes_dict = {}
    # # for valve in valves:
    # #     nodes_dict[valve] = Node(valve, valves[valve])
    # # for node in nodes_dict:
    # #     for tunnel in nodes_dict[node].TUNNELS:
    # #         nodes_dict[node].neighbours.append(nodes_dict[tunnel])
    # #     # print(nodes_dict[node])
    #
    # # nodes = list(nodes_dict.values())
    # # for node in nodes:
    # #     for neighbour in node.neighbours:
    # #         print(str(node) + " -> " + str(neighbour))
