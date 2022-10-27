import sys, heapq

def dijkstra():
    heap = []
    heapq.heappush(heap, (0, 1))
    cost[1] = 0
    while heap:
        weight, node = heapq.heappop(heap)

        for next_node, next_weight in adj[node]:
            tmp = weight + next_weight
            if cost[next_node] > tmp:
                cost[next_node] = tmp
                heapq.heappush(heap, (tmp, next_node))

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
cost = [sys.maxsize for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    adj[a].append((b,c))
    adj[b].append((a,c))

dijkstra()
print(cost[n])