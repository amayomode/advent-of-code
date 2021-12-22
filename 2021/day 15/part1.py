from parse_input import parseInput


def min_dist(dist, queue):
    small = float('inf')
    u = ''
    for v in queue:
        if dist[v] < small:
            small = dist[v]
            u = v
    return u


# Classic Dijkstra it is freakishly slow
def lowest_risk(Graph):
    queue = set()
    dist = {}
    rows, cols = Graph.shape
    for r in range(rows):
        for c in range(cols):
            dist[(r, c)] = float('inf')
            queue.add((r, c))
    dist[(0, 0)] = 0
    while queue:
        u = min_dist(dist, queue)
        queue.remove(u)
        if u == (rows-1, cols-1):
            return dist[(rows-1, cols-1)]
        for up, down in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            i = u[0] + up
            j = u[1] + down
            if (0 <= i <= rows - 1) and (0 <= j <= cols - 1):
                v = (i, j)
                if v in queue:
                    alt = dist[u] + Graph[v]
                    if alt < dist[v]:
                        dist[v] = alt
    return None


if __name__ == '__main__':
    Graph = parseInput("input.txt")
    print(lowest_risk(Graph))
