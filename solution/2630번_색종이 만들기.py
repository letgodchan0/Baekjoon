import sys
n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def check(x, y, n, num):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != num:
                return False
    return True

def dac(x, y, n, num):
    if check(x, y, n, num):
        if num:
            result[1] += 1
        else:
            result[0] += 1
    else:
        n //= 2
        dac(x, y, n, num)
        dac(x, y+n, n, arr[x][y+n])
        dac(x+n, y, n, arr[x+n][y])
        dac(x+n, y+n, n, arr[x+n][y+n])

result = {0:0, 1:0}
dac(0, 0, n, arr[0][0])
print(result[0])
print(result[1])
