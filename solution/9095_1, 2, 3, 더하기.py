dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4
T = int(input())
for _ in range(T):
    n = int(input())
    for i in range(4, n+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    print(dp[n])