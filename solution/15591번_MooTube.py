from collections import deque
import sys

def bfs(num):
    q = deque()
    visited = [0] * (N+1)
    visited[num] = 1
    for node, dist in adj[num]:
        visited[node] = 1
        q.append((node, dist))
    cnt = 0
    while q:
        node, dist = q.popleft()

        if dist >= k:
            cnt += 1
            for new_node, new_dist in adj[node]:
                if not visited[new_node]:
                    q.append((new_node, min(dist, new_dist)))
                    visited[new_node] = 1
    return cnt

N, Q = map(int, input().split())
adj = [[] for _ in range(N+1)]
d = [[] for _ in range(N+1)]
for _ in range(N-1):
    p, q, r = map(int, sys.stdin.readline().split())
    adj[p].append((q, r))
    adj[q].append((p, r))

for _ in range(Q):
    k, v = map(int, sys.stdin.readline().split())
    print(bfs(v))