import sys, heapq

def dijkstra(start, end):
    heap = []
    heapq.heappush(heap, [0, start])
    d[start] = 0
    while heap:
        check, i = heapq.heappop(heap)
        if start == end:
            return
        for v, w in adj[i]:
            tmp = w + check
            if d[v] > tmp:
                d[v] = tmp
                heapq.heappush(heap, [tmp, v])

V, E = map(int, input().split())
start = int(input())
adj = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    adj[u].append([v, w])

d = [100000000] * (V+1)

dijkstra(start, 3)

for i in range(1, V+1):
    print(d[i]) if d[i] < 100000000 else print('INF')