from parse_input import parseInput
from part1 import reflect, valid_point
import numpy as np


def fold_paper_completely(paper, instructions):
    for ins in instructions:
        new_paper = set()
        for coord in paper:
            if valid_point(coord, ins):
                new_paper.add(reflect(coord, ins))
            else:
                new_paper.add(coord)
        paper = new_paper
    return paper


def decode_output(paper, instructions):
    res = fold_paper_completely(paper, instructions)
    max_x = max(x[0] for x in res)
    max_y = max(y[1] for y in res)
    folded = np.zeros((max_x+1, max_y+1))
    for coord in res:
        folded[coord] = 1
    return np.array2string(folded.T > 0, separator='',
                           formatter={'bool': lambda x: ' █'[int(x)]})


if __name__ == '__main__':
    paper, instructions = parseInput("input.txt")
    res = decode_output(paper, instructions)
    print(res)
