from collections import Counter


def update(current_states):
    spawns = current_states[0]
    for i in range(8):
        current_states[i] = current_states[i + 1]
    current_states[6] += spawns
    current_states[8] = spawns
    return current_states


def simulate(initial_states, days):
    current_states = {i: 0 for i in range(9)}
    current_states.update(Counter(initial_states))
    for _ in range(days):
        current_states = update(current_states)
    return sum(current_states.values())


def parseInput(filename):
    with open(filename, "r") as f:
        return [int(i) for i in f.readline().strip().split(",")]


if __name__ == "__main__":
    initial_states = parseInput("input.txt")
    print(simulate(initial_states, 80))
