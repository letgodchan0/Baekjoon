from collections import deque

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    maps = [list(map(int, input().split())) for _ in range(m)]
    visited = [[0] * n for _ in range(m)]
    cnt = 0
    for i in range(m):
        for j in range(n):
            if maps[i][j] == 1 and not visited[i][j]:
                cnt += 1
                q = deque([])
                q.append((i, j))
                visited[i][j] = 1
                while q:
                    x, y = q.popleft()
                    # 상, 하, 좌, 우, 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래
                    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0,1], [-1, -1], [-1, 1], [1, -1], [1, 1]]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and maps[nx][ny] == 1:
                            q.append((nx, ny))
                            visited[nx][ny] = 1
    print(cnt)
