import sys
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
numbers = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
lst = [0] * (n*n+1)

for i in range(n):
    for j in range(n):
        lst[i*n + j + 1] = lst[i*n + j] + arr[i][j]

for num in numbers:
    x1, y1, x2, y2 = num
    tmp = 0
    for i in range(x1-1,x2):
        tmp += lst[i*n+y2] - lst[i*n+y2-(y2-y1+1)]

    print(tmp)