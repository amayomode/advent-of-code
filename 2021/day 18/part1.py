from snailfish import magnitude, add, reduce
from parse_input import parse_input


def part1(input_lines: list) -> int:
    final_sum = ""
    while input_lines:
        line1 = input_lines.pop(0)
        if not final_sum:
            line2 = input_lines.pop(0)
            final_sum = f"{line1} + {line2}"
        else:
            final_sum = f"{final_sum} + {line1}"
        final_sum = reduce(add(final_sum))

    return magnitude(final_sum)


if __name__ == '__main__':
    input_lines = parse_input("input.txt")
    print(part1(input_lines))
