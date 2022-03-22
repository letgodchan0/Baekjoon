def bfs():
    q = [0] * (m*n*h)
    front = -1
    rear = -1
    # 안익은 토마토 개수
    cnt = 0
    day = 0
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if tomato[k][i][j] == 1:
                    rear += 1
                    q[rear] = (k, i, j)
                elif tomato[k][i][j] == 0:
                    cnt += 1
    if cnt == 0:
        return 0
    while front != rear:
        front += 1
        k, i, j = q[front]
        for dk, di, dj in [[-1, 0, 0], [1, 0, 0], [0, -1, 0, ], [0, 1, 0], [0, 0, -1], [0, 0, 1]]:
            nk, ni, nj = k + dk, i + di, j + dj
            if 0 <= nk < h and 0 <= ni < n and 0 <= nj < m and tomato[nk][ni][nj] == 0 and visited[nk][ni][nj] == 0:
                visited[nk][ni][nj] = visited[k][i][j] + 1
                cnt -= 1
                if visited[nk][ni][nj] > day:
                    day = visited[nk][ni][nj]
                rear += 1
                q[rear] = (nk, ni, nj)
    if cnt != 0:
        return -1
    else:
        return day

m, n, h = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[0] * m for _ in range(n)] for _ in range(h)]
print(bfs())
