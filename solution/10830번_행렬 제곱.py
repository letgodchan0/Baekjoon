import sys
n, b = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def matrix(matrix1, matrix2):
    answer = [[0]*n for _ in range(n)]
    matrix2 = list(zip(*matrix2))
    for i in range(n):
        for j in range(n):
            tmp = 0
            for k in range(n):
                tmp += matrix1[i][k] * matrix2[j][k]
            answer[i][j] = tmp % 1000
    return answer

check = {}
def power(base, exponent):
    if int(exponent) in check:
        return check[int(exponent)]

    if exponent == 1:
        for i in range(n):
            for j in range(n):
                base[i][j] %= 1000
        check[int(exponent)] = base
        return base

    if exponent % 2 == 0:
        newbase = power(base, exponent / 2)
        check[int(exponent)] = matrix(newbase, newbase)
        return matrix(newbase, newbase)
    else:
        newbase = power(base, (exponent - 1) / 2)
        check[int(exponent)] = matrix(matrix(newbase, newbase), base)
        return matrix(matrix(newbase, newbase), base)

arr = power(arr, b)
for num in check[b]:
    print(*num)