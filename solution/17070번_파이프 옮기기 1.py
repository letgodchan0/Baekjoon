def dfs(x, y, type):
    global cnt
    if x == n-1 and y == n-1:
        cnt += 1
        return


    if type == 0 or type == 2:
        if y + 1 < n:
            if not arr[x][y+1]:
                dfs(x, y+1, 0)

    if type == 1 or type == 2:
        if x + 1 < n:
            if not arr[x+1][y]:
                dfs(x+1, y, 1)

    if type == 0 or type == 1 or type == 2:
        if x + 1 < n and y + 1 < n:
            if not arr[x+1][y] and not arr[x][y+1] and not arr[x+1][y+1]:
                dfs(x+1, y+1, 2)

import sys
n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cnt = 0
dfs(0, 1, 0)
print(cnt)