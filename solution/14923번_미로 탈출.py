from collections import deque
import sys

def bfs(x, y):
    q = deque([(x, y, 0)])
    visited[x][y][0] = 1
    while q:
        x, y, check = q.popleft()
        if x == ex-1 and y == ey-1:
            return visited[x][y][check] - 1

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not arr[nx][ny] and not visited[nx][ny][check]:
                q.append((nx, ny, check))
                visited[nx][ny][check] = visited[x][y][check] + 1

            elif 0 <= nx < n and 0 <= ny < m and arr[nx][ny] and not visited[nx][ny][check] and not check:
                q.append((nx, ny, check+1))
                visited[nx][ny][check+1] = visited[x][y][check] + 1
    return -1

n, m = map(int, input().split())
sx, sy = map(int, input().split())
ex, ey = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
print(bfs(sx-1, sy-1))