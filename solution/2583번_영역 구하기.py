from collections import deque
import sys
def bfs(i, j):
    q = deque([])
    q.append((i,j))
    cnt = 1
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in [[-1,0], [1,0], [0,-1], [0,1]]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == 0 and not visited[nx][ny]:
                cnt += 1
                q.append((nx, ny))
                visited[nx][ny] = 1
    return cnt


m, n, k = map(int, input().split())
arr = [[0] * n for _ in range(m)]
visited = [[0] * n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    start = m - y2
    for i in range(start, start + y2-y1):
        for j in range(x1, x2):
            arr[i][j] = 1

count = 0
result = []
ans = 0
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0 and not visited[i][j]:
            ans = bfs(i, j)
            if ans:
                count += 1
                result.append(ans)
print(count)
result.sort()
print(*result)
