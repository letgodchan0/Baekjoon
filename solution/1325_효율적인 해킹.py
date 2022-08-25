from collections import deque
import sys
def bfs(start):
    q = deque([])
    q.append((start))
    visited = [0] * (n+1)
    visited[start] = 1
    cnt = 1
    while q:
        x = q.popleft()
        for dx in adj[x]:
            if not visited[dx]:
                q.append(dx)
                visited[dx] = 1
                cnt += 1
    return cnt

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adj[b].append(a)

res = 0
lst = []
for i in range(1, n+1):
    check = bfs(i)
    if check > res:
        res = check
    lst.append((check, i))

for result, idx in lst:
    if result == res:
        print(idx, end =' ')