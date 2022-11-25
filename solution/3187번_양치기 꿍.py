from collections import deque
import sys

def bfs(x,y):
    q = deque([(x,y)])
    visited[x][y] = 1
    k, v = 0, 0
    while q:
        x, y = q.popleft()
        if arr[x][y] == "v":
            v += 1
        elif arr[x][y] == "k":
            k += 1

        for dx, dy in [(-1,0),(1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and arr[nx][ny] != "#":
                q.append((nx, ny))
                visited[nx][ny] = 1

    return (k, 0) if k > v else (0, v)

r, c = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
visited = [[0] * (c) for _ in range(r)]
sheep, wolf = 0, 0
for i in range(r):
    for j in range(c):
        if arr[i][j] != "#" and not visited[i][j]:
            k, v = bfs(i, j)
            sheep += k
            wolf += v

print(sheep, wolf)