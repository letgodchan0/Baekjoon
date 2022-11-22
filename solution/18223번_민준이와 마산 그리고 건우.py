import sys, heapq

def dijkstra(start, end):
    heap = []
    heapq.heappush(heap, (start, 0))
    cost = [100000000] * (n + 1)
    cost[start] = 0
    while heap:
        node, weight = heapq.heappop(heap)

        for cur_node, cur_weight in adj[node]:
            tmp = cur_weight + weight
            if cost[cur_node] > tmp:
                cost[cur_node] = tmp
                heapq.heappush(heap, (cur_node, tmp))
    return cost[end]

n, m, p = map(int, input().split())

adj = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    adj[u].append((v, w))
    adj[v].append((u, w))

one = dijkstra(1, n)
two = dijkstra(1, p) + dijkstra(p, n)
if one < two:
    print("GOOD BYE")
else:
    print("SAVE HIM")