from collections import deque
import sys

def bfs():
    q = deque([(x1-1, y1-1)])
    visited = [[0] * m for _ in range(n)]

    while q:
        x, y = q.popleft()

        if x == x2-1 and y == y2-1:
            return visited[x][y]

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            for i in range(1, k+1):
                nx, ny = x + dx * i, y + dy * i

                if nx < 0 or nx >= n or ny <0 or ny >= m or arr[nx][ny] == '#':
                    break

                if not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                elif visited[nx][ny] > visited[x][y]:
                    continue
                else:
                    break

    return -1

input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
x1, y1, x2, y2 = map(int, input().split())

print(bfs())