import sys, heapq

def dijkstra(start, end, is_check):
    heap = []
    heapq.heappush(heap, [0, start])
    d = [INF] * (n+1)
    d[start] = 0
    if is_check:
        while heap:
            check, i = heapq.heappop(heap)
            if d[i] < check:
                continue

            for v, w in adj[i]:
                tmp = check + w
                if d[v] > tmp:
                    d[v] = tmp
                    heapq.heappush(heap, [tmp, v])
    else:
        while heap:
            check, i = heapq.heappop(heap)
            if d[i] < check:
                continue
            for v, w in adj[i]:
                if v == y:
                    continue
                tmp = check + w
                if d[v] > tmp:
                    d[v] = tmp
                    heapq.heappush(heap, [tmp, v])

    return d
n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]

INF = sys.maxsize
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    adj[u].append((v, w))
x, y, z = map(int, input().split())
res = dijkstra(x, y, True)[y] + dijkstra(y, z, True)[z]
res = res if res < INF else -1
print(res, end = ' ')
ans = dijkstra(x, z, False)[z]
print(ans if ans < INF else -1)