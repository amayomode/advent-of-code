import numpy as np


def parseInput(filename):
    Graph = []
    with open(filename, "r") as f:
        for line in f.readlines():
            Graph.append([int(i) for i in line.strip()])
    Graph = np.array(Graph)
    return Graph


if __name__ == '__main__':
    Graph = parseInput("input.txt")
    print(Graph)
