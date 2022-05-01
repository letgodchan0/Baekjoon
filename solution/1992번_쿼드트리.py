import sys
n = int(input())
arr = [list(map(int, sys.stdin.readline().strip('\n'))) for _ in range(n)]


def check(x, y, n, num):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != num:
                return False
    return True

def dac(x, y, n, num):
    global ans
    if check(x, y, n, num):
        ans += str(num)
    else:
        n //= 2
        ans += '('
        dac(x, y, n, num)
        dac(x, y+n, n, arr[x][y+n])
        dac(x+n, y, n, arr[x+n][y])
        dac(x+n, y+n, n, arr[x+n][y+n])
        ans += ')'

ans = ''
dac(0, 0, n, arr[0][0])
print(ans)
