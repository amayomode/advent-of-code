from part1 import parseInput, update_grid
import numpy as np


def syncronized_step(grid):
    i = 1
    while True:
        grid = update_grid(grid)
        if np.all(grid == 0):
            return i
        i += 1


if __name__ == '__main__':
    grid = parseInput("input.txt")
    print(syncronized_step(grid))
