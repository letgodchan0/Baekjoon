from collections import deque
import sys

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

n, m = map(int, input().split())
arr = [list(map(int, list(sys.stdin.readline().split()))) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

res = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] and not visited[i][j]:
            bfs(i, j)
            res += 1
print(res)