string1 = input()
string2 = input()

dp = [[0] * 4001 for _ in range(4001)]
answer = 0
for i in range(1, len(string1)+1):
    for j in range(1, len(string2)+1):
        if string1[i-1] == string2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            answer = max(dp[i][j], answer)
print(answer)