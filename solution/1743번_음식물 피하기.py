from collections import deque
import sys
def bfs(x, y):
    q = deque([])
    q.append((x, y))
    visited = [[0] * m for _ in range(n)]
    cnt = 0
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1
    return cnt

n, m, k = map(int, input().split())
arr = [[0] * m for _ in range(n)]
lst = []
for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    arr[a-1][b-1] = 1
    lst.append((a-1,b-1))

res = 0
for x, y in lst:
    tmp = bfs(x, y)
    res = tmp if tmp > res else res
print(res)