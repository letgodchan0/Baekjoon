from collections import deque
import sys

def bfs(x,y):
    q = deque([(x,y)])
    visited[x][y] = 1
    cnt_sheep, cnt_wolf = 0, 0
    while q:
        x, y = q.popleft()
        if arr[x][y] == "o":
            cnt_sheep += 1
        elif arr[x][y] == 'v':
            cnt_wolf += 1

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny]  != "#" and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1

    if cnt_wolf >= cnt_sheep:
        cnt_sheep = 0
    else:
        cnt_wolf = 0

    return cnt_sheep, cnt_wolf

r, c = map(int, input().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]

sheep, wolf = 0, 0
for i in range(r):
    for j in range(c):
        if arr[i][j] != '#' and not visited[i][j]:
            s, w = bfs(i, j)
            sheep += s
            wolf += w

print(sheep, wolf)