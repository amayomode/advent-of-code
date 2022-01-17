def parseInput(filename):
    with open(filename, "r") as f:
        target_area = []
        for x in f.read().strip().split(", "):
            target_area.append(tuple(int(i)
                               for i in x[x.index("=") + 1:].split("..")))
        return target_area


if __name__ == "__main__":
    print(parseInput("input.txt"))
