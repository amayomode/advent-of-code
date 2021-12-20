def parseInput(filename):
    paper, instructions = [], []
    with open('input.txt', 'r') as f:
        data = f.readlines()
        ind = data.index("\n")
        for line in data[:ind]:
            paper.append(tuple(int(i) for i in line.strip().split(',')))
        for ins in data[ind+1:]:
            a, b = ins.strip().split("=")
            instructions.append((a[-1], int(b)))
    return paper, instructions


if __name__ == '__main__':
    paper, instructions = parseInput('input.txt')
