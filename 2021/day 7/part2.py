from part1 import parseInput


def lowest_fuel(positions):
    best = float("inf")
    for median in range(min(positions), max(positions)):
        cost = 0
        for pos in positions:
            n = abs(median - pos)
            cost += n * (n + 1) / 2
        if cost <= best:
            best = cost
    return best


if __name__ == "__main__":
    positions = parseInput("input.txt")
    print(lowest_fuel(positions))
