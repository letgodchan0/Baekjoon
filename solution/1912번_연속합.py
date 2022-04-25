import sys
n = int(input())
lst = list(map(int, sys.stdin.readline().split()))
dp = [0] * n
dp[0] = ans = lst[0]
for i in range(1, n):
    dp[i] = max(lst[i], lst[i]+dp[i-1])
    if dp[i] > ans:
        ans = dp[i]
print(ans)