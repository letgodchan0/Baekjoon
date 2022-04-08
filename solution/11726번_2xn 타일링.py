number = int(input())
dp = [0] * 1001
dp[1], dp[2] = 1, 2
for num in range(3, number+1):
    dp[num] = dp[num-2] + dp[num - 1]
print(dp[number]%10007)