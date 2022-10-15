from collections import deque
import sys

n, m = map(int, input().split())
indegree = [0] * (n+1)
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    indegree[b] += 1

q = deque([])
for i in range(1, n+1):
    if not indegree[i]:
        q.append(i)
res = []
while q:
    x = q.popleft()
    res.append(x)
    for i in adj[x]:
        indegree[i] -= 1
        if not indegree[i]:
            q.append(i)

for i in range(1, n+1):
    if i not in res:
        res.append(i)
print(*res)
