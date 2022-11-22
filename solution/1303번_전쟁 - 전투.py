from collections import deque
import sys

def bfs(x,y, check):
    q = deque([(x,y)])
    visited[x][y] = 1
    cnt = 1
    while q:
        x, y = q.popleft()

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == check and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] += 1
                cnt += 1
    return cnt

n, m = map(int, input().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(m)]
visited = [[0] * n for _ in range(m)]
me, you = 0, 0
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            if arr[i][j] == 'W':
                tmp = bfs(i, j, 'W')
                me += tmp ** 2
            else:
                tmp = bfs(i, j, 'B')
                you += tmp ** 2

print(me, you)