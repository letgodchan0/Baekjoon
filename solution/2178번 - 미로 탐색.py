def bfs():
    q = [[0,0]]
    visited[0][0] = 1
    while q:
        i, j = q.pop(0)
        for di, dj in [[-1,0], [1,0], [0,-1], [0,1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and maze[ni][nj] == 1 and visited[ni][nj] == 0:
                q.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1
    return visited[n-1][m-1]


n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
print(bfs())