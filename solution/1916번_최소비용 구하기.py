import sys, heapq

def dijkstra(start, end):
    heap = []
    heapq.heappush(heap, [0, start])
    d[start] = 0

    while heap:
        check, i = heapq.heappop(heap)

        if i == end:
            return d[end]

        for v, w in adj[i]:
            tmp = w + check
            if d[v] > tmp:
                d[v] = tmp
                heapq.heappush(heap, [tmp, v])

n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    adj[u].append([v, w])

start, end = map(int, input().split())

d = [100000000] * (n+1)
print(dijkstra(start, end))