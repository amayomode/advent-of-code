from parse_input import parseInput
from collections import defaultdict


def step(pairs, rules):
    new_pairs = defaultdict(int)
    for k in pairs:
        new_pairs[k[0] + rules[k]] += pairs[k]
        new_pairs[rules[k] + k[1]] += pairs[k]
    return new_pairs


def pair_insertions(template, rules, steps):
    # generate pairs
    pairs = defaultdict(int)
    for i in range(len(template) - 1):
        pairs[template[i:i+2]] += 1

    # polymerize stepwise updating the number of pairs
    for _ in range(steps):
        pairs = step(pairs, rules)

    # count elements
    elem_counts = defaultdict(int)
    elem_counts[template[-1]] = 1
    for k, v in pairs.items():
        elem_counts[k[0]] += v
    # return sum of max - min count
    return max(elem_counts.values()) - min(elem_counts.values())


if __name__ == '__main__':
    template, rules = parseInput("input.txt")
    print(pair_insertions(template, rules, 10))
