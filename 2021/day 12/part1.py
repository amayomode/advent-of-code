from collections import defaultdict


def distinct_paths(map, vertex, visited, complete):
    for neighbor in map[vertex]:
        if neighbor in visited:
            continue
        if neighbor == "end":
            complete.append(1)
            continue
        if neighbor.islower():
            visited.add(neighbor)
        distinct_paths(map, neighbor, visited, complete)
        if neighbor.islower():
            visited.discard(neighbor)
    return sum(complete)


def parseInput(filename):
    map = defaultdict(list)
    with open(filename, "r") as f:
        for line in f.readlines():
            k, v = line.strip().split("-")
            map[k].append(v)
            map[v].append(k)
    for k, v in map.items():
        map[k] = [i for i in v if i != "start"]
    map.pop('end')
    return map


if __name__ == "__main__":
    map = parseInput("input.txt")
    print(distinct_paths(map, "start", set(), list()))
