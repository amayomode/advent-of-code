import numpy as np


def find_risk_level(heightmap):
    risk_level = 0
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
                risk_level += 1 + point
    return risk_level


def parseInput(filename):
    with open('input.txt', 'r') as f:
        output = []
        for line in f.readlines():
            output.append([int(i) for i in line.strip()])
        return np.array(output)


if __name__ == '__main__':
    heightmap = parseInput('input.txt')
    print(find_risk_level(heightmap))
