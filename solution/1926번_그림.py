import sys
from collections import deque
def bfs(x, y):
    q = deque([])
    q.append((x, y))
    visited[x][y] = 1
    cnt = 1
    while q:
        i, j = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] and not visited[ni][nj]:
                visited[ni][nj] = 1
                q.append((ni, nj))
                cnt += 1
    return cnt

n, m = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split()))for _ in range(n)]
visited = [[0] * m for _ in range(n)]
result = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not visited[i][j]:
            result.append(bfs(i, j))

print(len(result))
print(max(result)) if result else print(0)