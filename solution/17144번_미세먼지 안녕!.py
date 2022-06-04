from collections import deque

def bfs(x, y):
    q = deque([])
    q.append((x, y))
    while q:
        x, y = q.popleft()
        tmp = 0
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] >= 0:
                tmp += arr[x][y] // 5
                visited[nx][ny] += arr[x][y] // 5
    visited[x][y] += arr[x][y] - tmp

r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
for i in range(r):
    if arr[i][0] == -1:
        up = i
        down = i + 1
        break
cnt = 0
for _ in range(t):
    visited = [[0] * c for _ in range(r)]
    cnt += 1
    # 미세먼지 확산
    for i in range(r):
        for j in range(c):
            if arr[i][j] > 0:
                bfs(i, j)
    tmp1, tmp2 = visited[up][-1], visited[down][-1]
    for i in range(c - 1, 1, -1):
        visited[up][i] = visited[up][i - 1]
        visited[down][i] = visited[down][i - 1]
    visited[up][1], visited[down][1] = 0, 0

    # 공기청정기 바람 방향 위로
    tmp3, tmp4 = visited[0][-1], visited[-1][-1]
    for i in range(up - 1):
        visited[i][-1] = visited[i + 1][-1]
    visited[up - 1][-1] = tmp1
    for i in range(r - 1, down + 1, -1):
        visited[i][-1] = visited[i - 1][-1]
    visited[down + 1][-1] = tmp2

    # 공기청정기 바람 방향 <-
    tmp5, tmp6 = visited[0][0], visited[-1][0]
    for i in range(c - 2):
        visited[0][i] = visited[0][i + 1]
        visited[-1][i] = visited[-1][i + 1]
    visited[0][-2] = tmp3
    visited[-1][-2] = tmp4

    # 공기청정기 바람 방향 아래
    for i in range(up - 1, 1, -1):
        visited[i][0] = visited[i - 1][0]
    visited[1][0] = tmp5
    for i in range(down + 1, r - 2):
        visited[i][0] = visited[i + 1][0]
    visited[-2][0] = tmp6

    visited[up][0] = -1
    visited[down][0] = -1

    arr = visited

result = 0
for i in range(r):
    for j in range(c):
        result += arr[i][j]
print(result+2)