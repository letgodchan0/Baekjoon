from collections import deque
import sys

def melting():
    glacier = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                cnt = 0
                for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and not arr[ni][nj]:
                        cnt += 1
                glacier[i][j] = cnt
    for i in range(n):
        for j in range(m):
            arr[i][j] -= glacier[i][j]
            if arr[i][j] < 0:
                arr[i][j] = 0

def dfs(x,y):
    stack = deque([])
    stack.append((x, y))
    visited[x][y] = 1
    while stack:
        x, y = stack.pop()
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] and not visited[nx][ny]:
                stack.append((nx, ny))
                visited[nx][ny] = 1

n, m = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
res = 0
while True:
    visited = [[0] * m for _ in range(n)]
    melting()
    cnt = 0
    check = 0
    res += 1
    for i in range(n):
        for j in range(m):
            if arr[i][j] and not visited[i][j]:
                dfs(i, j)
                cnt += 1
                check += 1
    if cnt > 1:
        print(res)
        break
    if not check:
        print(0)
        break