def parseInput(filename):
    with open(filename, "r") as f:
        return [int(i) for i in f.read().strip().split(",")]


def lowest_fuel(positions):
    positions.sort()
    median = positions[len(positions) // 2]
    cost = 0
    for pos in positions:
        cost += abs(median - pos)
    return cost


if __name__ == "__main__":
    positions = parseInput("input.txt")
    print(lowest_fuel(positions))
