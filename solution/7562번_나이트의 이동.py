from collections import deque
def bfs(x, y):
    q = deque([])
    q.append((x, y))
    visited = [[0] * l for _ in range(l)]
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        if x == e1 and y == e2:
            return visited[e1][e2] - 1

        for dx, dy in  [(-2,-1), (-1,-2), (1,-2), (2,-1), (-2, 1), (-1, 2), (1, 2), (2, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1


t = int(input())
for _ in range(t):
    l = int(input())
    arr = [[0] * l for _ in range(l)]
    s1, s2 = map(int, input().split())
    e1, e2 = map(int, input().split())
    print(bfs(s1, s2))