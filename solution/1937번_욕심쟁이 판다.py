import sys
sys.setrecursionlimit(1000000)

def dfs(x,y):
    if visited[x][y] == -1:
        visited[x][y] = 0

        for dx, dy in [(-1,0), (1,0), (0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > arr[x][y]:
                visited[x][y] = max(visited[x][y], dfs(nx, ny))

    return visited[x][y] + 1

n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[-1] * n for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i,j))
print(answer)


""" 시간초과!
from collections import deque
import sys

def dfs(i,j):
    stack = deque([])
    stack.append((i,j,1))
    res = 0
    while stack:
        x, y, cnt = stack.pop()
        res = cnt if cnt > res else res
        for dx, dy in [(-1,0), (1,0), (0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > arr[x][y]:
                if visited[nx][ny]:
                    res = cnt + visited[nx][ny] if cnt + visited[nx][ny] > res else res
                else:
                    stack.append((nx, ny, cnt+1))

    visited[i][j] = res
    return res

n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(n):
        tmp = dfs(i,j)
        answer = tmp if tmp > answer else answer
print(answer)
"""