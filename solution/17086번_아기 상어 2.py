from collections import deque
import sys

def bfs(x,y):
    q = deque([])
    q.append((x, y, 0))
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1
    while q:
        x, y, cnt = q.popleft()
        if arr[x][y]:
            return cnt

        for dx, dy in [(-1,0),(-1,1),(-1,-1),(0,-1),(0,1),(1,0),(1,-1),(1,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                q.append((nx, ny, cnt + 1))
                visited[nx][ny] = 1

n, m = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

res = 0
for i in range(n):
    for j in range(m):
        res = max(res, bfs(i,j))

print(res)