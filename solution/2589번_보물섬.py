from collections import deque
import sys
def bfs(x, y):
    q = deque([])
    q.append((x, y, 0))
    visited = [[0] * w for _ in range(l)]
    visited[x][y] = 1
    check = 0
    while q:
        x, y, cnt = q.popleft()
        check = cnt if cnt > check else check
        for dx, dy in  [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < l and 0 <= ny < w and not visited[nx][ny] and arr[nx][ny] == 'L':
                q.append((nx, ny, cnt + 1))
                visited[nx][ny] = 1
    return cnt

l, w = map(int, input().split())
arr = [list(sys.stdin.readline()) for _ in range(l)]
res = 0
for i in range(l):
    for j in range(w):
        if arr[i][j] == 'L':
            dis = bfs(i, j)
            res = dis if dis > res else res
print(res)