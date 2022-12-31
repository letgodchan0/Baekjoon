from collections import deque
import sys

n, m, r = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(n+1)]
visited = [0] * (n+1)
result = [0] * (n+1)
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

q = deque([r])
visited[r], dist = 1, 1
result[r] = dist
while q:
    node = q.popleft()

    for new in sorted(adj[node]):
        if not visited[new]:
            q.append(new)
            visited[new] = 1
            dist += 1
            result[new] = dist

for i in range(1, n+1):
    print(result[i])
