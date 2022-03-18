# bfs로 풀기
def bfs(i, j):
    q = []
    q.append((i,j))
    visited[i][j] = 1
    cnt = 0
    while q:
        i, j = q.pop(0)
        cnt += 1
        for di, dj in [[-1,0], [1,0], [0,-1], [0,1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj <n and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1
    return cnt

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
result = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and visited[i][j] == 0:
            result.append(bfs(i, j))
print(len(result))
result.sort()
for ans in result:
    print(ans)



## dfs로 풀기
def dfs(i, j):
    visited[i][j] = 1
    cnt = 1
    for di, dj in [[-1,0], [1,0], [0,-1], [0,1]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] ==1 and visited[ni][nj] == 0:
            cnt += dfs(ni, nj)
    return cnt

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
result = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and visited[i][j] == 0:
            result.append(dfs(i, j))

print(len(result))
result.sort()
for ans in result:
    print(ans)
