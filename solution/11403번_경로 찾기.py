from collections import deque
import sys

def bfs(x):
    q = deque([])
    q.append(x)
    visited = [[0] * n for _ in range(n)]
    lst = []
    while q:
        i = q.popleft()
        for k in range(n):
            if arr[i][k] and not visited[i][k]:
                visited[i][k] = 1
                lst.append(k)
                q.append(k)
    for j in lst:
        answer[x][j] = 1

n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = [[0] * n for _ in range(n)]
for i in range(n):
    bfs(i)
for ans in answer:
    print(*ans)
