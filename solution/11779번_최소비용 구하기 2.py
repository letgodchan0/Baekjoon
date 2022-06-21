import sys, heapq

def dijkstra(start, end):
    heap = []
    heapq.heappush(heap, [0, start, [start]])
    d[start] = 0
    while heap:
        check, i, lst = heapq.heappop(heap)
        if i == end:
            return d[end], lst
        for v, w in adj[i]:
            tmp = w + check
            if d[v] > tmp:
                d[v] = tmp
                heapq.heappush(heap, [tmp, v, lst + [v]])

V = int(input())
E = int(input())
adj = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    adj[u].append([v, w])

start, end = map(int, input().split())
d = [100000000] * (V+1)
answer, lst = dijkstra(start, end)

print(answer)
print(len(lst))
print(*lst)
