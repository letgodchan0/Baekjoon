# pypy
from collections import deque
import sys
def bfs(x, y):
    q = deque([])
    q.append((x, y))
    visited = [[False]*m for _ in range(n)]
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        # 뚫려있음
        if x == 0 or x == n-1 or y == 0 or y == m-1:
            return 1
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not cheese[nx][ny] and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
    return 0
n, m = map(int, input().split())
cheese = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cnt = 0
while True:
    lst = []
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 1:
                tmp = 0
                for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and cheese[ni][nj] == 0:
                        tmp += bfs(ni, nj)
                        if tmp >= 2:
                            lst.append((i,j))
                            break
    for x, y in lst:
        cheese[x][y] = 0
    cnt += 1
    check = 0
    for ch in cheese:
        check += sum(ch)
    if check == 0:
        print(cnt)
        break


# python

import sys
from collections import deque

def bfs(x, y):
    q = deque([])
    q.append((0,0))
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    while q:
        x, y = q.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if cheese[nx][ny]:
                    cheese[nx][ny] += 1
                else:
                    visited[nx][ny] = 1
                    q.append((nx,ny))

n, m = map(int, input().split())
cheese = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cnt = 0
while True:
    bfs(0, 0)
    check = True
    for i in range(n):
        for j in range(m):
            if cheese[i][j] >= 3:
                cheese[i][j] = 0
            elif cheese[i][j] > 0:
                cheese[i][j] = 1
                check = False
    cnt += 1
    if check:
        print(cnt)
        break
