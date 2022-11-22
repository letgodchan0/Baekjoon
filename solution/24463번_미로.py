import sys
sys.setrecursionlimit(10000000)
def dfs(x, y):
    if x == end1 and y == end2:
        return True

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == '@':
            arr[nx][ny] = '.'
            if dfs(nx, ny):
                return True
            arr[nx][ny] = '@'
    return False
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
res = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == ".":
            if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                res.append((i, j))
            arr[i][j] = "@"

start1, start2 = res[0]
end1, end2 = res[1]

answer = dfs(start1, start2)
arr[start1][start2] = '.'

for i in arr:
    print(''.join(i))