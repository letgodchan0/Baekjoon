import sys
sys.setrecursionlimit(10**8)

def dfs(x, y):
    if x == n-1 and y == m-1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    check = 0
    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] < arr[x][y]:
            check += dfs(nx, ny)

    dp[x][y] = check

    return dp[x][y]

n, m = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]
print(dfs(0,0))