import sys

def check(idx, start, n, m):
    if idx == m:
        print(' '.join(map(str, result)))
        return 

    for i in range(start, n):
        result.append(arr[i])

        check(idx + 1, i, n, m)

        result.pop()

n, m = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

result = []

check(0, 0, n, m)