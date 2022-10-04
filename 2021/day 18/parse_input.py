def parse_input(filename: str) -> list:
    with open(filename, "r") as f:
        input_lines = []
        for line in f.read().splitlines():
            input_lines.append(line)
    return input_lines


if __name__ == "__main__":
    print(parse_input("input.txt"))
