from parse_input import parseInput


def reflect(coord, instruction):
    k = instruction[1]
    if instruction[0] == "y":
        return (coord[0], 2 * k - coord[1])
    else:
        return (2*k - coord[0], coord[1])


def valid_point(coord, instruction):
    if instruction[0] == "y":
        return coord[1] > instruction[1]
    else:
        return coord[0] > instruction[1]


def fold_paper_once(paper, instructions):
    new_paper = set()
    for coord in paper:
        if valid_point(coord, instructions[0]):
            new_paper.add(reflect(coord, instructions[0]))
        else:
            new_paper.add(coord)
    return len(new_paper)


if __name__ == '__main__':
    paper, instructions = parseInput("input.txt")
    #print(reflect((6, 0), ("x", 5)))
    print(fold_paper_once(paper, instructions))
