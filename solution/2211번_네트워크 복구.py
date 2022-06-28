import sys, heapq

def dijkstra(start):
    heap = []
    heapq.heappush(heap, [0, start])
    d = [INF] * (n+1)
    d[start] = 0
    while heap:
        cur_cost, cur_node = heapq.heappop(heap)

        if d[cur_node] < cur_cost:
            continue

        for v, w in adj[cur_node]:
            tmp = cur_cost + w
            if d[v] > tmp:
                d[v] = tmp
                lst[v] = cur_node
                heapq.heappush(heap, [tmp, v])
n, m = map(int, input().split())
INF = int(1e9)
adj = [[] for _ in range(n+1)]
lst = [0] * (n+1)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    adj[a].append((b,c))
    adj[b].append((a,c))

dijkstra(1)
print(n-1)
for i in range(2, n+1):
    print(i, lst[i])