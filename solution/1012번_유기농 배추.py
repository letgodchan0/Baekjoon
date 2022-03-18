# dfs로 풀기
def dfs(i, j):
    visited[i][j] = 1
    for di, dj in [[-1,0], [1,0], [0,-1], [0,1]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m and arr[i][j] == 1 and visited[ni][nj] == 0:
            dfs(ni, nj)

import sys
sys.setrecursionlimit(111111)
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(k)]
    arr = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    for i, j in data:
        arr[j][i] = 1
    answer = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j)
                answer += 1
    print(answer)

# bfs로 풀기
def bfs(i, j):
    q = []
    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        for di, dj in [[-1,0], [1,0], [0,-1], [0,1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and arr[i][j] == 1 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append((ni, nj))
t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(k)]
    arr = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    for i, j in data:
        arr[j][i] = 1

    answer = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)
                answer += 1
    print(answer)