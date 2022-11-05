from collections import deque
import sys

def bfs(x, y):
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

n, m = map(int, input().split())
arr = [list(map(int, list(sys.stdin.readline().split()))) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

res = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if not visited[i][j] and arr[i][j] == 1:
            visited[i][j] = -1

for i in visited:
    print(*i)