import sys, heapq

def dijkstra():
    heap = []
    heapq.heappush(heap, [0, 0])
    d = [INF] * (n)
    d[0] = 0
    while heap:
        cur_cost, cur_node = heapq.heappop(heap)

        if d[cur_node] < cur_cost:
            continue

        for v, w in adj[cur_node]:
            if v != n-1 and lst[v]:
                continue
            tmp = cur_cost + w
            if d[v] > tmp:

                d[v] = tmp
                heapq.heappush(heap, [tmp, v])
    return d

n, m = map(int, input().split())
lst = list(map(int, sys.stdin.readline().split()))
adj = [[] for _ in range(n)]
INF = sys.maxsize
for _ in range(m):
    a, b, t = map(int, sys.stdin.readline().split())
    adj[a].append((b,t))
    adj[b].append((a,t))

res = dijkstra()
print(res[n-1] if res[n-1] < INF else -1)