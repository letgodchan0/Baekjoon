def bfs():
    q = [0] * (m*n)
    front = -1
    rear = -1
    # 안익은 토마토 개수
    cnt = 0
    day = 0
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 1:
                rear += 1
                q[rear] = (i, j)
                visited[i][j] = 1
            elif tomato[i][j] == 0:
                cnt += 1
    if cnt == 0:
        return 0
    while front != rear:
        front += 1
        i, j = q[front]
        for di, dj in [[-1,0], [1,0], [0,-1], [0,1]]:
            ni, nj = i + di, j + dj

            if 0 <= ni < n and 0 <= nj < m and tomato[ni][nj] == 0 and visited[ni][nj] == 0:
                visited[ni][nj] = visited[i][j] + 1
                cnt -= 1
                if visited[ni][nj] > day:
                    day = visited[ni][nj]
                rear += 1
                q[rear] = (ni, nj)
    if cnt != 0:
        return -1
    else:
        return day - 1

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
print(bfs())
