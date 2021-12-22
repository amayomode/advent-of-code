from parse_input import parseInput
import heapq


def find_cost(i, j, Graph):
    rows, cols = Graph.shape
    start = Graph[i % rows, j % cols]
    for _ in range(i//rows):
        start = (start % 9) + 1
    for _ in range(j//cols):
        start = (start % 9) + 1
    return start


# Speed things up with a priority queue
# O(n) creation O(log n) pop and push
def lowest_risk_faster(Graph, expansion):
    rows, cols = map(lambda x: x*expansion, Graph.shape)
    p_queue = [(0, 0, 0)]
    heapq.heapify(p_queue)
    dist = {}
    visited = set()
    while p_queue:
        cost, r, c = heapq.heappop(p_queue)
        u = (r, c)
        if u == (rows-1, cols-1):
            return cost
        if u in visited:
            continue
        visited.add(u)
        dist[u] = cost
        for up, down in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            i = u[0] + up
            j = u[1] + down
            if (0 <= i <= rows - 1) and (0 <= j <= cols - 1):
                heapq.heappush(
                    p_queue, (dist[u] + find_cost(i, j, Graph), i, j)
                )
    return None


if __name__ == '__main__':
    Graph = parseInput("input.txt")
    '''for j in range(0, 50):
        print(find_cost(0, j, Graph), end=" ")'''
    print(lowest_risk_faster(Graph, 5))
