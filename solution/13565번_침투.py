from collections import deque
import sys

def dfs(x, y):
    stack = deque([])
    stack.append((x,y))
    visited[x][y] = 1
    while stack:
        x, y = stack.pop()

        if x == m-1:
            return True

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not arr[nx][ny] and not visited[nx][ny]:
                stack.append((nx, ny))
                visited[nx][ny] = 1
    return False

m, n = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().replace('\n', ''))) for _ in range(m)]
visited = [[0] * n for _ in range(m)]
check = False
for i in range(n):
    if not arr[0][i] and dfs(0, i):
        check = True

print('YES' if check else 'NO')