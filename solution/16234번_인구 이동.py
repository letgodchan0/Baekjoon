from collections import deque
import sys

def bfs(x, y):
    q = deque([])
    q.append((x,y))
    visited[x][y] = 1
    res = []
    while q:
        x, y = q.popleft()
        res.append([x,y])
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and abs(arr[x][y] - arr[nx][ny]) >= l and abs(arr[x][y] - arr[nx][ny]) <= r and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1
    return res
n, l, r = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cnt = 0
while True:
    check = True
    visited = [[0] * n for _ in range(n)]
    help = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                result = bfs(i,j)
                if len(result) > 1:
                    check = False
                    tmp = sum(map(lambda x : arr[x[0]][x[1]], result))
                    help.append([len(result), tmp, result])
    if check:
        break
    cnt += 1
    for length, value, lst in help:
        for x, y in lst:
            arr[x][y] = value // length

print(cnt)