from part1 import parseInput, simulate

if __name__ == "__main__":
    initial_states = parseInput("input.txt")
    print(simulate(initial_states, 256))
