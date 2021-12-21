from part1 import parseInput, pair_insertions

if __name__ == '__main__':
    template, rules = parseInput("input.txt")
    print(pair_insertions(template, rules, steps=40))
