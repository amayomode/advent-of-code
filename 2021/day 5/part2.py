is_perpendicular = lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1]


def line_equation(coordinate):
    a = coordinate[0]
    b = coordinate[1]
    m = (a[1] - b[1]) / (a[0] - b[0])
    c = a[1] - m * a[0]
    return m, c


def generate_points(coordinate):
    a = coordinate[0]
    b = coordinate[1]
    points = []
    if is_perpendicular(coordinate):
        if a[0] == b[0]:
            y1 = min(a[1], b[1])
            y2 = max(a[1], b[1]) + 1
            points = [(a[0], y) for y in range(y1, y2)]
        if a[1] == b[1]:
            x1 = min(a[0], b[0])
            x2 = max(a[0], b[0]) + 1
            points = [(x, a[1]) for x in range(x1, x2)]
    else:
        m, c = line_equation(coordinate)
        x1 = min(a[0], b[0])
        x2 = max(a[0], b[0]) + 1
        points = [(x, int(m * x + c)) for x in range(x1, x2)]
    return points


def generate_grid(coordinates):
    grid = {}
    for coord in coordinates:
        for point in generate_points(coord):
            grid.setdefault(point, 0)
            grid[point] += 1
    return grid


def count_intersections(coordinates):
    grid = generate_grid(coordinates)
    count = 0
    for k, v in grid.items():
        if v >= 2:
            count += 1
    return count


def parseInput(filename):
    with open(filename, "r") as f:
        coordinates = []
        for line in f.readlines():
            a, b = line.split("->")
            a = tuple(int(i) for i in a.strip().split(","))
            b = tuple(int(i) for i in b.strip().split(","))
            coordinates.append((a, b))
        return coordinates


if __name__ == "__main__":
    coordinates = parseInput("input.txt")
    print(count_intersections(coordinates))
