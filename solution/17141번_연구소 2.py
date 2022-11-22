from collections import deque
from itertools import combinations
import sys, copy

def bfs(x, y, tmp):
    q = deque([])
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not tmp[nx][ny] and visited[nx][ny] != '-':
                if not visited[nx][ny] or visited[nx][ny] > visited[x][y] + 1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    
n, m = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
viruses, res = [], sys.maxsize
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            viruses.append((i,j))
viruses = list(combinations(viruses, m))

for virus in viruses:
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                visited[i][j] = '-'
    
    tmp = copy.deepcopy(arr)
    for x in range(n):
        for y in range(n):
            if tmp[x][y] == 2 and (x, y) not in virus:
                tmp[x][y] = 0

    for x, y in virus:
        bfs(x, y, tmp)

    cnt, answer = 0, -1

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                cnt += 1
            if visited[i][j] != '-':
                answer = max(answer, visited[i][j])

    if cnt == m:
        res = min(res, answer)

print(-1 if res == sys.maxsize else res)
