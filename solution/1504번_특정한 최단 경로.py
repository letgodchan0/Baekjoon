import sys, heapq

def dijkstra(start, end):
    heap = []
    heapq.heappush(heap, (0, start))
    d = [INF] * (n + 1)
    d[start] = 0

    while heap:
        check, i = heapq.heappop(heap)
        if i == end:
            return d[end]

        for v, w in adj[i]:
            tmp = check + w
            if d[v] > tmp:
                d[v] = tmp
                heapq.heappush(heap, [tmp, v])
    return INF
n, e = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    adj[a].append((b,c))
    adj[b].append((a,c))

v1, v2 = map(int, input().split())
INF = int(1e9)


first = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
second = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)
answer = min(first, second)

print(answer if answer < INF else -1)