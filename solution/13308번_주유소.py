import sys, heapq

def dijkstra():
    dist = [[sys.maxsize] * (max(city) + 1) for _ in range(n+1)]
    heap, dist[1][city[1]] = [], 0
    heapq.heappush(heap, (0, 1, city[1]))
    while heap:
        weight, node, cost = heapq.heappop(heap)

        if node == n:
            return weight

        for next_node, next_weight in adj[node]:
            new_cost = min(cost, city[next_node])
            if dist[next_node][cost] > weight + cost * next_weight:
                dist[next_node][cost] = weight + cost * next_weight
                heapq.heappush(heap, (weight + cost * next_weight, next_node, new_cost))


n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
city = [0] + list(map(int, sys.stdin.readline().split()))
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    adj[u].append((v,w))
    adj[v].append((u,w))

print(dijkstra())
