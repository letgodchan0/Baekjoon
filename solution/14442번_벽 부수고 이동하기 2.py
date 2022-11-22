from collections import deque
import sys

def bfs():
    q = deque([])
    q.append((0,0,K))
    visited[0][0][K] = 1
    while q:
        x, y, k = q.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y][k]

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not arr[nx][ny] and not visited[nx][ny][k]:
                q.append((nx,ny,k))
                visited[nx][ny][k] = visited[x][y][k] + 1

        if k > 0:
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] and not visited[nx][ny][k-1]:
                    q.append((nx, ny, k-1))
                    visited[nx][ny][k-1] = visited[x][y][k] + 1
    return -1

n, m, K = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[[0 for _ in range(11)] for _ in range(m)] for _ in range(n)]

print(bfs())