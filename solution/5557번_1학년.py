n = int(input())
numbers = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(n)]

dp[0][numbers[0]] = 1

for i in range(n-1):
    for j in range(21):
        if dp[i][j]:
            if j + numbers[i+1] <= 20: dp[i+1][j+numbers[i+1]] += dp[i][j]
            if 0 <= j - numbers[i+1]: dp[i+1][j-numbers[i+1]] += dp[i][j]

for i in dp:
    print(i)

print(dp[-2][numbers[-1]])