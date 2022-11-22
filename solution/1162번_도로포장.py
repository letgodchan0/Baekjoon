import sys, heapq

def dijkstra(start):
    heap, INF, cnt = [], sys.maxsize, 0
    weights = [[INF] * (k+1) for _ in range(n+1)]
    heapq.heappush(heap, (0, start, cnt))
    weights[start][cnt] = 0
    while heap:
        weight, node, cnt = heapq.heappop(heap)
        if weights[node][cnt] < weight:
            continue

        for next_node, cost in adj[node]:
            tmp = weight + cost
            if weights[next_node][cnt] > tmp:
                weights[next_node][cnt] = tmp
                heapq.heappush(heap, (tmp, next_node, cnt))

            if cnt < k and weights[next_node][cnt+1] > weight:
                # 여기서 도로 포장!
                weights[next_node][cnt+1] = weight
                heapq.heappush(heap, (weight, next_node, cnt+1))
    return min(weights[n])

n, m, k = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    adj[a].append((b,c))
    adj[b].append((a,c))

print(dijkstra(1))