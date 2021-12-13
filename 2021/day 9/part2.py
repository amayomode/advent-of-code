from part1 import parseInput
from math import prod


def find_basin(low_point, heightmap):
    stack = [low_point]
    visited = []
    rows, cols = heightmap.shape
    while stack:
        point = stack.pop()
        i, j = point
        if point not in visited:
            visited.append(point)
            # up
            if i-1 >= 0:
                if heightmap[i-1, j] < 9:
                    stack.append((i-1, j))
            # down
            if i+1 <= rows - 1:
                if heightmap[i+1, j] < 9:
                    stack.append((i+1, j))
            # left
            if j-1 >= 0:
                if heightmap[i, j-1] < 9:
                    stack.append((i, j-1))
            # right
            if j+1 <= cols - 1:
                if heightmap[i, j+1] < 9:
                    stack.append((i, j+1))
    return visited


def find_basin_lengths(heightmap):
    basin_lengths = []
    rows, cols = heightmap.shape
    for i in range(rows):
        for j in range(cols):
            neighbors = []
            point = heightmap[i, j]
            # up
            if i-1 >= 0:
                neighbors.append(heightmap[i-1, j])
            # down
            if i+1 <= rows - 1:
                neighbors.append(heightmap[i+1, j])
            # left
            if j-1 >= 0:
                neighbors.append(heightmap[i, j-1])
            # right
            if j+1 <= cols - 1:
                neighbors.append(heightmap[i, j+1])
            if all([point < n for n in neighbors]):
                basin_lengths.append(len(find_basin((i, j), heightmap)))
    return basin_lengths


if __name__ == '__main__':
    heightmap = parseInput('input.txt')
    basin = find_basin_lengths(heightmap)
    basin.sort(reverse=True)
    print(prod(basin[:3]))
