n = int(input())
lst = [0] * 10000
for i in range(n):
    lst[i] = int(input())
dp = [0] * 10000
dp[0] = lst[0]
dp[1] = lst[0] + lst[1]
dp[2] = max(lst[0] + lst[2], lst[1] + lst[2], dp[1])

for i in range(3, n):
    dp[i] = max(dp[i-2] + lst[i], dp[i-3] + lst[i-1] + lst[i], dp[i-1])

print(max(dp))