import sys, heapq

def dijkstra():
    heap = []
    cost = [sys.maxsize] * (n+1)
    cost[start] = 0
    heapq.heappush(heap, (0, 0, start))
    while heap:
        cur_weight, weight, node = heapq.heappop(heap)

        if node == end:
            return cur_weight

        for new_node, new_weight in adj[node]:
            if new_weight <= weight:
                continue

            tmp = new_weight + cur_weight
            cost[new_node] = min(cost[new_node], tmp)
            heapq.heappush(heap, (tmp, new_weight, new_node))

    return "DIGESTA"

n, m = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    adj[a].append((b,c))
    adj[b].append((a,c))
start, end = map(int, sys.stdin.readline().split())

print(dijkstra())