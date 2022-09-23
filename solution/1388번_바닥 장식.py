from collections import deque

def bfs(i, j):
    q = deque([])
    q.append((i, j))
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[i][j] == arr[nx][ny]:
                if arr[i][j] == '-' and nx == i:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                elif arr[i][j] == '|' and ny == j:
                    q.append((nx, ny))
                    visited[nx][ny] = 1

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
res = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            bfs(i, j)
            res += 1
print(res)