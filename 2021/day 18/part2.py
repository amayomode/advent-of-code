from snailfish import magnitude, add, reduce
from parse_input import parse_input
import itertools


def part2(input_lines: list) -> int:
    max_magnitude = 0
    pairs = list(itertools.permutations(input_lines, 2))
    for pair in pairs:
        final_sum = reduce(add(f"{pair[0]} + {pair[1]}"))
        current_magnitude = magnitude(final_sum)
        if current_magnitude > max_magnitude:
            max_magnitude = current_magnitude
    return max_magnitude


if __name__ == '__main__':
    input_lines = parse_input("input.txt")
    print(part2(input_lines))
