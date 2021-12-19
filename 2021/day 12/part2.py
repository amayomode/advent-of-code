from part1 import parseInput


def distinct_paths(map, vertex, visited, complete, revisited_cave):
    for neighbor in map[vertex]:
        if neighbor == "end":
            complete.append(1)
            continue
        if neighbor.islower():
            if neighbor in visited:
                if revisited_cave != "":
                    continue
                revisited_cave = neighbor
            else:
                visited.add(neighbor)
        distinct_paths(map, neighbor, visited, complete, revisited_cave)
        if neighbor.islower():
            if revisited_cave == neighbor:
                revisited_cave = ""
            else:
                visited.discard(neighbor)
    return sum(complete)


if __name__ == "__main__":
    map = parseInput("input.txt")
    print(distinct_paths(map, "start", set(), list(), ''))
