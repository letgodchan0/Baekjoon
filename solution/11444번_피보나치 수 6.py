import sys
n = int(sys.stdin.readline())
arr = [[1, 1], [1, 0]]

def matrix(matrix1, matrix2):
    answer = [[0]*2 for _ in range(2)]
    matrix2 = list(zip(*matrix2))
    for i in range(2):
        for j in range(2):
            tmp = 0
            for k in range(2):
                tmp += matrix1[i][k] * matrix2[j][k]
            answer[i][j] = tmp % 1000000007
    return answer

check = {}
def power(base, exponent):
    if exponent == 1:
        for i in range(len(base)):
            for j in range(len(base)):
                base[i][j] %= 1000000007
        return base

    if exponent % 2:
        newbase = power(base, (exponent-1)//2)
        return matrix(matrix(newbase, newbase), base)
    else:
        newbase = power(base, exponent//2)
        return matrix(newbase, newbase)
arr = power(arr, n)
print(1) if n < 3 else print(arr[1][0])