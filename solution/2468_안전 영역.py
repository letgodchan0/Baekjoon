from collections import deque
import sys
def bfs(x, y, num):
    q = deque([])
    q.append((x, y))
    visited[x][y] = 1
    while q:
        i, j = q.popleft()
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0,1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] >= num and not visited[ni][nj]:
                q.append((ni, nj))
                visited[ni][nj] = 1

n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
lst = []
for i in range(n):
    for j in range(n):
        if arr[i][j] not in lst:
            lst.append(arr[i][j])
result = []
for num in lst:
    cnt = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] >= num and not visited[i][j]:
                bfs(i, j, num)
                cnt += 1
    result.append(cnt)
print(max(result))