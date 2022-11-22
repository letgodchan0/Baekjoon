from collections import deque
import sys

n, m = map(int, input().split())
indegree, outdegree = [0] * (n+1), [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    outdegree[a].append(b)
    indegree[b] += 1

q = deque([])
for i in range(1, n+1):
    if not indegree[i]:
        q.append((i, 1))

res = []
answer = [0] * (n+1)
while q:
    x, semester = q.popleft()
    res.append((x,semester))
    for num in outdegree[x]:
        indegree[num] -= 1
        if not indegree[num]:
            q.append((num, semester+1))

for n, s in res:
    answer[n] = s
print(*answer[1:])