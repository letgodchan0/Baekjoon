from collections import deque
import sys, copy

def bfs(x, y):
    tmp = k+1
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and array[nx][ny] != 0:
            tmp = min(tmp, arr[nx][ny])
    if tmp != k+1:
        arr[x][y] = tmp

n, k = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
s, x, y = map(int, input().split())

cnt = 0
while cnt < s:
    check = False
    array = copy.deepcopy(arr)
    for i in range(n):
        for j in range(n):
            if array[i][j] == 0:
                check = True
                bfs(i,j)
    cnt += 1
    if not check:
        break

print(arr[x-1][y-1])