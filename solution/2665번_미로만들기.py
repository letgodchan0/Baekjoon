from collections import deque
import sys

def bfs():
    q = deque([(0,0)])
    visited = [[0] * n for _ in range(n)]
    visited[0][0] = 1

    while q:
        x, y = q.popleft()

        if x == n-1 and y == n-1:
            return visited[x][y] - 1

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if arr[nx][ny]:
                    q.appendleft((nx,ny))
                    visited[nx][ny] = visited[x][y]
                else:
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1

n = int(input())
arr = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]

print(bfs())