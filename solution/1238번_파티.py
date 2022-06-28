import sys, heapq

def dijkstra(start):
    heap = []
    heapq.heappush(heap, [0, start])
    d = [INF] * (n + 1)
    d[start] = 0
    while heap:
        check, i = heapq.heappop(heap)

        for v, w in adj[i]:
            tmp = check + w
            if d[v] > tmp:
                d[v] = tmp
                heapq.heappush(heap, [tmp, v])

    return d
n, m, x = map(int, sys.stdin.readline().split())
INF = int(1e9)

adj = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    adj[u].append([v, w])

answer = 0
result = dijkstra(x)
for i in range(1, n+1):
    res = dijkstra(i)
    if answer < res[x] + result[i]:
        answer = res[x] + result[i]
print(answer)

