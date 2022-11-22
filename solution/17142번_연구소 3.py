from collections import deque
from itertools import combinations
import sys

def bfs(virus):
    q = deque([])
    visited = [[-1] * n for _ in range(n)]

    for i, j in virus:
        q.append((i,j))
        visited[i][j] = 0

    answer = 0
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not arr[nx][ny] and visited[nx][ny] == -1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    answer = max(answer, visited[nx][ny])
                elif arr[nx][ny] == 2 and visited[nx][ny] == -1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

    res = list(sum(visited, [])).count(-1)
    if res == check:
        return answer
    return sys.maxsize

n, m = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
check, viruses = 0, []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            viruses.append((i,j))
        elif arr[i][j] == 1:
            check += 1

viruses = list(combinations(viruses, m))
answer = sys.maxsize
for virus in viruses:
    answer = min(answer, bfs(virus))

print(-1 if answer == sys.maxsize else answer)