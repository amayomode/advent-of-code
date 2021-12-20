from collections import defaultdict


def distinct_paths(map, vertex, visited):
    if vertex == "end":
        return 1
    if vertex.islower():
        visited.add(vertex)
    count = 0
    for neighbor in map[vertex]:
        if neighbor not in visited:
            count += distinct_paths(map, neighbor, visited)
    if vertex.islower():
        visited.discard(vertex)
    return count


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
    print(distinct_paths(map, "start", set()))
