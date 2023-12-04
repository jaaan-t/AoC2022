def print_grid(grid: list):
    line = ""
    for r in range(len(grid)):
        line += str(r).zfill(3) + " "
        for c in range(len(grid[r])):
            line += grid[r][c]
        line += "\n"
    print(line)


def get_dims(sensor_beacons: list):
    x_max = -float('inf')
    y_max = -float('inf')
    x_min = float('inf')
    y_min = float('inf')
    for pair in sensor_beacons:
        s_x, s_y = pair[0][0], pair[0][1]
        b_x, b_y = pair[1][0], pair[1][1]
        x_max = max(s_x, b_x, x_max)
        y_max = max(s_y, b_y, y_max)
        x_min = min(s_x, b_x, x_min)
        y_min = min(s_y, b_y, y_min)
    return x_max, y_max, x_min, y_min


def mark_detection(sensors_beacons: list, covered: set, y_target: int):
    for pair in sensors_beacons:
        s_x, s_y = pair[0][0], pair[0][1]
        b_x, b_y = pair[1][0], pair[1][1]
        distance = abs(s_x - b_x) + abs(s_y - b_y)
        # print(pair, distance)
        for r in range(0, distance + 1):
            if s_y + r == y_target:
                for c in range(distance - r + 1):
                    covered.add((s_x + c, s_y + r))
                for c in range(0, -distance + r - 1, -1):
                    covered.add((s_x + c, s_y + r))
        for r in range(-distance, 1):
            if s_y + r == y_target:
                for c in range(distance + r + 1):
                    covered.add((s_x + c, s_y + r))
                for c in range(0, -distance - r - 1, -1):
                    covered.add((s_x + c, s_y + r))


def mark_detection_2(sensors_beacons: list, covered: set, x_max: int, y_max: int):
    for pair in sensors_beacons:
        s_x, s_y = pair[0][0], pair[0][1]
        b_x, b_y = pair[1][0], pair[1][1]
        dist = abs(s_x - b_x) + abs(s_y - b_y)
        # print(pair, dist)

        for r in range(max(0, min(s_y, y_max)), max(0, min(s_y + dist, y_max)) + 1):
            for c in range(max(0, min(s_x, x_max)), max(0, min(s_x + dist - r + s_y, x_max)) + 1):
                covered.add((c, r))
            for c in range(max(0, min(s_x, x_max)), max(0, min(s_x - dist + r - s_y, x_max)) - 1, -1):
                covered.add((c, r))

        for r in range(max(0, min(s_y, y_max)), max(0, min(s_y - dist, y_max)) - 1, -1):
            for c in range(max(0, min(s_x, x_max)), max(0, min(s_x + dist + r - s_y, x_max)) + 1):
                covered.add((c, r))
            for c in range(max(0, min(s_x, x_max)), max(0, min(s_x - dist - r + s_y, x_max)) - 1, -1):
                covered.add((c, r))


def mark_detection_edges(sensors_beacons: list, x_max: int, y_max: int):
    edges = set()

    for pair in sensors_beacons:
        s_x, s_y = pair[0][0], pair[0][1]
        b_x, b_y = pair[1][0], pair[1][1]
        dist = abs(s_x - b_x) + abs(s_y - b_y)
        # print(pair, dist)

        for r in range(s_y, s_y + dist + 1):
            if 0 <= r <= y_max:
                c = s_x + dist - r + s_y
                if 0 <= c <= x_max:
                    edges.add((c, r))
                c = s_x - dist + r - s_y
                if 0 <= c <= x_max:
                    edges.add((c, r))

        for r in range(s_y, s_y - dist - 1, -1):
            if 0 <= r <= y_max:
                c = s_x + dist + r - s_y
                if 0 <= c <= x_max:
                    edges.add((c, r))

                c = max(0, min(s_x - dist - r + s_y, x_max)) - 1
                if 0 <= c <= x_max:
                    edges.add((c, r))

    return edges


def find_sensor_edges(pair: list, x_max: int, y_max: int):
    edges = []

    s_x, s_y = pair[0][0], pair[0][1]
    b_x, b_y = pair[1][0], pair[1][1]
    dist = abs(s_x - b_x) + abs(s_y - b_y)
    # print(pair, dist)

    for r in range(s_y, s_y + dist + 1):
        c = s_x + dist - r + s_y
        edges.append((c, r))
        c = s_x - dist + r - s_y
        edges.append((c, r))

    for r in range(s_y, s_y - dist - 1, -1):
        c = s_x + dist + r - s_y
        edges.append((c, r))
        c = s_x - dist - r + s_y
        edges.append((c, r))

    return edges


def make_square(sensor: tuple, edges: list):
    s_x, s_y = sensor
    min_x = 99999999999
    min_y = 99999999999
    max_x = -99999999999
    max_y = -99999999999
    for edge in edges:
        x, y = edge
        min_x = int(min(x, min_x))
        min_y = int(min(y, min_y))
        max_x = int(max(x, max_x))
        max_y = int(max(y, max_y))

    square = [(s_x, min_y),
              (max_x, s_y),
              (s_x, max_y),
              (min_x, s_y)]

    return square


def is_inside_square(point: tuple, square: list, edges: list) -> bool:
    p_x, p_y = point

    if point in edges:
        return True

    (s_x, min_y), (max_x, s_y), (s_x, max_y), (min_x, s_y) = square

    if p_x < min_x or p_x > max_x or p_y < min_y or p_y > max_y:
        return False

    A = s_x, min_y
    B = max_x, s_y
    C = s_x, max_y
    D = min_x, s_y
    # print(A, B, C, D)

    A_to_B = []
    y = min_y
    for x in range(s_x, max_x + 1):
        A_to_B.append((x, y))
        y += 1
    # print(A_to_B)

    B_to_C = []
    y = s_y
    for x in range(max_x, s_x - 1, -1):
        B_to_C.append((x, y))
        y += 1
    # print(B_to_C)

    C_to_D = []
    y = max_y
    for x in range(s_x, min_x - 1, -1):
        C_to_D.append((x, y))
        y -= 1
    # print(C_to_D)

    D_to_A = []
    y = s_y
    for x in range(min_x, s_x + 1):
        D_to_A.append((x, y))
        y -= 1
    # print(D_to_A)

    for x, y in A_to_B:
        if p_y == y and not p_x <= x or p_x == x and not p_y >= y:
            return False
    for x, y in B_to_C:
        if p_y == y and not p_x <= x or p_x == x and not p_y <= y:
            return False
    for x, y in C_to_D:
        if p_y == y and not p_x >= x or p_x == x and not p_y <= y:
            return False
    for x, y in D_to_A:
        if p_y == y and not p_x >= x or p_x == x and not p_y >= y:
            return False

    return True


def get_edges_plus_one(sensor: tuple, edges: list):
    square = make_square(sensor, edges)
    (s_x, min_y), (max_x, s_y), (s_x, max_y), (min_x, s_y) = square

    edges_plus_one = []

    A = s_x, min_y
    B = max_x, s_y
    C = s_x, max_y
    D = min_x, s_y
    # print(A, B, C, D)

    edges_plus_one.append((A[0], A[1] - 1))
    edges_plus_one.append((B[0] + 1, B[1]))
    edges_plus_one.append((C[0], C[1] + 1))
    edges_plus_one.append((D[0] - 1, D[1]))

    A_to_B = []
    y = min_y
    for x in range(s_x, max_x + 1):
        A_to_B.append((x, y))
        y += 1
    # print(A_to_B)

    B_to_C = []
    y = s_y
    for x in range(max_x, s_x - 1, -1):
        B_to_C.append((x, y))
        y += 1
    # print(B_to_C)

    C_to_D = []
    y = max_y
    for x in range(s_x, min_x - 1, -1):
        C_to_D.append((x, y))
        y -= 1
    # print(C_to_D)

    D_to_A = []
    y = s_y
    for x in range(min_x, s_x + 1):
        D_to_A.append((x, y))
        y -= 1
    # print(D_to_A)

    for x, y in A_to_B:
        edges_plus_one.append((x + 1, y))
    for x, y in B_to_C:
        edges_plus_one.append((x + 1, y))
    for x, y in C_to_D:
        edges_plus_one.append((x - 1, y))
    for x, y in D_to_A:
        edges_plus_one.append((x - 1, y))

    return edges_plus_one


def find_nearest_sensor(point: tuple, sensors: list):
    px, py = point
    min_dist = 99999999999
    x, y = px, py
    for sx, sy in sensors:
        dist = (abs(px - sx) ** 2 + abs(py - sy) ** 2) ** 0.5
        min_dist = min(min_dist, dist)
        if min_dist == dist:
            x, y = sx, sy
    return x, y


def get_input(day: int, test: int):
    file = "input"
    if test:
        file = "test"
    with open(file + str(day)) as f:
        return f.read().strip().split("\n")


if __name__ == '__main__':
    ###############################
    DAY = 15
    TEST = 0
    INPUT = get_input(DAY, TEST)
    ###############################

    sensors_beacons = []
    sensor_with_beacons = {}
    sensors = []
    beacons = []
    for line in INPUT:
        a = line.split(" ")
        s_x = int(a[2].split("=")[1].split(",")[0])
        s_y = int(a[3].split("=")[1].split(":")[0])
        b_x = int(a[8].split("=")[1].split(",")[0])
        b_y = int(a[9].split("=")[1])
        sensor = (s_x, s_y)
        beacon = (b_x, b_y)
        sensors_beacons.append([sensor, beacon])
        sensor_with_beacons[sensor] = beacon
        sensors.append(sensor)
        beacons.append(beacon)

    x_max, y_max, x_min, y_min = get_dims(sensors_beacons)
    width = x_max - x_min + 1
    height = y_max - y_min + 1

    # Part 1
    covered = set()
    y_target = 2000000
    mark_detection(sensors_beacons, covered, y_target)
    for s in sensors:
        if s in covered:
            covered.remove(s)
    for b in beacons:
        if b in covered:
            covered.remove(b)
    x = []
    for item in covered:
        if item[1] == y_target:
            x.append(item[0])
    print(len(x))

    # Part 2
    mult = 4000000
    edges = set()
    edges_plus_one = {}
    squares = []
    x_max = mult
    y_max = mult
    found = []
    found_and_nearest_sensor = []
    counter = 0
    for pair in sensors_beacons:
        counter += 1
        print(counter/25, end=" ")
        sensor = pair[0]
        sensor_edges = find_sensor_edges(pair, x_max, y_max)
        sensor_edges_plus_one = get_edges_plus_one(sensor, sensor_edges)
        for edge in sensor_edges:
            edges.add(edge)
        for edge in sensor_edges_plus_one:
            if 0 <= edge[0] <= x_max and 0 <= edge[1] <= y_max:
                count = 1
                if edge in edges_plus_one and edge not in edges:
                    count = edges_plus_one[edge] + 1
                    edges_plus_one[edge] = count
                else:
                    edges_plus_one[edge] = count
    counter = 0
    for edge in edges_plus_one:
        counter += 1
        if counter % 1000000 == 0:
            print(counter / 1000000, end=" ")
        count = edges_plus_one[edge]
        if count >= 4 and edge not in edges:
            found.append(edge)

    for point in found:
        nearest_sensor = find_nearest_sensor(point, sensors)
        found_and_nearest_sensor.append((point, nearest_sensor))

    for item in found_and_nearest_sensor:
        point, nearest_sensor = item
        pair = [nearest_sensor, sensor_with_beacons[nearest_sensor]]
        sensor_edges = find_sensor_edges(pair, x_max, y_max)
        square = make_square(nearest_sensor, sensor_edges)
        if not is_inside_square(point, square, sensor_edges):
            # print("found:", point, "sensor:", nearest_sensor)
            print(point[0]*mult + point[1])
            break

    # grid = []
    # for i in range(0, 30):
    #     grid.append(["."] * (50))
    # for x in range(0, 50):
    #     for y in range(0, 30):
    #         for pair in sensors_beacons:
    #             sensor = pair[0]
    #             sensor_edges = find_sensor_edges(pair, x_max, y_max)
    #             square = make_square(sensor, sensor_edges)
    #             if is_inside_square((x, y), square, sensor_edges):
    #                 grid[y][x] = "#"
    # for c in edges:
    #     x, y = c
    #     if x >= 0 and y >= 0:
    #         grid[y][x] = "*"
    # for c in edges_plus_one:
    #     #     print(c)
    #     x, y = c
    #     if x >= 0 and y >= 0:
    #         grid[y][x] = "O"
    # print_grid(grid)
