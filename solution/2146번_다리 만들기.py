from collections import deque
import sys

def bfs(x, y):
    global cnt
    cnt += 1
    q = deque([])
    q.append((x,y))
    visited[x][y] = cnt
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = cnt

def bfs2(i,j):
    q = deque([])
    q.append((i, j, 0))
    visited2 = [[0] * n for _ in range(n)]
    visited2[i][j] = 1
    while q:
        x, y, check = q.popleft()
        if visited[x][y] and (visited[x][y] != visited[i][j]):
            return check - 1
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited2[nx][ny]:
                q.append((nx, ny, check + 1))
                visited2[nx][ny] = 1
    return 10001
n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] and not visited[i][j]:
            bfs(i, j)

res = 10001
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            tmp = bfs2(i,j)
            res = tmp if res > tmp else res
print(res)
