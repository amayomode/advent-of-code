def parseInput(filename):
    with open(filename, "r") as f:
        template, lines = f.read().strip().split("\n\n")
        rules = {}
        for line in lines.split("\n"):
            k, v = line.split('->')
            rules[k.strip()] = v.strip()
    return template, rules


if __name__ == "__main__":
    template, rules = parseInput("input.txt")
