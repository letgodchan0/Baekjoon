from collections import deque
import sys

def bfs():
    q = deque([(0,0)])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1

    while q:
        x, y = q.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y] - 1

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if not arr[nx][ny]:
                    q.appendleft((nx,ny))
                    visited[nx][ny] = visited[x][y]
                else:
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1

m, n = map(int, input().split())
arr = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]

print(bfs())