import numpy as np


def parseInput(filename):
    with open(filename, "r") as f:
        grid = []
        for line in f.readlines():
            grid.append([int(i) for i in line.strip()])
        return np.array(grid)


def valid(pos, grid):
    rows, cols = grid.shape
    i, j = pos
    return (i >= 0 and i <= rows - 1) and (j >= 0 and j <= cols - 1)


def find_neighbors(pos, grid):
    i, j = pos
    neighbors = [
        (i-1, j), (i+1, j), (i, j-1), (i, j+1),
        (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)
    ]
    return [c for c in neighbors if valid(c, grid)]


def update_grid(grid):
    # update energy level
    grid = (grid + 1) % 10
    # find flashing octopi
    flashing = np.where(grid == 0)
    stack = list(zip(flashing[0], flashing[1]))
    visited = []
    while stack:
        pos = stack.pop()
        if pos not in visited:
            visited.append(pos)
            for neighbor in find_neighbors(pos, grid):
                if grid[neighbor] != 0:
                    grid[neighbor] = (grid[neighbor] + 1) % 10
                    if (grid[neighbor]) == 0:
                        stack.append(neighbor)
    return grid


def count_flashes(grid, steps):
    count = 0
    for _ in range(steps):
        grid = update_grid(grid)
        count += np.count_nonzero(grid == 0)
    return count


if __name__ == "__main__":
    grid = parseInput("input.txt")
    print(count_flashes(grid, 100))
