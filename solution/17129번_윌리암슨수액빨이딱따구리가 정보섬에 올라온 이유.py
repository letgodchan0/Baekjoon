import sys
from collections import deque

def bfs(x,y):
    q = deque([])
    q.append([x,y])
    visited[x][y]+=1
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 1 and not visited[nx][ny]:
                    q.append([nx,ny])
                    visited[nx][ny]= visited[x][y] +1
                    if arr[nx][ny] in (3,4,5):
                        print('TAK')
                        print(visited[x][y])
                        exit()
    print('NIE')

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]


for i in range(n):
    for j in range(m):
        if arr[i][j]==2:
            bfs(i,j)