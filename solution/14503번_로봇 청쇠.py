from collections import deque
import sys

def bfs(sx, sy, d):
    q = deque([(sx, sy, d)])
    visited = [[0] * m for _ in range(n)]
    visited[sx][sy] = 1
    cnt = 1
    while q:
        x, y, d = q.popleft()

        if d == 0:dx, dy, dd = 0, -1, 3
        elif d == 1:dx, dy, dd = -1, 0, -1
        elif d == 2:dx, dy, dd = 0, 1,  -1
        else:dx, dy, dd = 1, 0, -1

        nx, ny, nd = x + dx, y + dy, d + dd

        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and not arr[nx][ny]:
                q.append((nx, ny, nd))
                visited[nx][ny] = visited[x][y] + 1
                cnt += 1
            elif (not visited[x-1][y] and not arr[x-1][y]) or (not visited[x+1][y] and not arr[x+1][y]) or (not visited[x][y-1] and not arr[x][y-1]) or (not visited[x][y+1] and not arr[x][y+1]):
                q.append((x, y, nd))
            else:
                if d == 0:
                    ox, oy = 1, 0
                elif d == 1:
                    ox, oy = 0, -1
                elif d == 2:
                    ox, oy = -1, 0
                else:
                    ox, oy = 0, 1

                nx, ny = x + ox, y + oy

                if 0 <= nx < n and 0 <= ny < m and not arr[nx][ny]:
                    q.append((nx, ny, d))
    return cnt

n, m = map(int, input().split())
sx, sy, d = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(bfs(sx, sy, d))