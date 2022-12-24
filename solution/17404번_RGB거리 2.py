import sys

n = int(input())
dp = [[0] * 3 for _ in range(n)]
arr = [[] for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, sys.stdin.readline().split()))
answer = sys.maxsize
for k in range(3):
    dp[0] = [sys.maxsize] * 3
    dp[0][k] = arr[0][k]

    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]

    for i in range(3):
        if i != k:
            answer = min(answer, dp[n-1][i])
print(answer)