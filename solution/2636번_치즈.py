import sys
from collections import deque

def check(arr):
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                return False
    return True

def bfs():
    q = deque([])
    q.append((0,0))
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    remove = []
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if arr[nx][ny] == 1:
                    remove.append((nx, ny))
                else:
                    q.append((nx, ny))
                visited[nx][ny] = 1
    for i, j in remove:
        arr[i][j] = 0
    return len(remove)

n, m = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

lst = []
cnt = 0
while not check(arr):
    lst.append(bfs())
    cnt += 1
print(cnt)
print(lst[-1])