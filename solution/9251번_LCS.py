s1 = input()
s2 = input()

dp = [[0] * (len(s2)+1) for _ in range(len(s1)+1)]
stack1 = []
for i in range(1, len(s1)+1):
    stack1.append(s1[i-1])
    stack2 = []
    for j in range(1, len(s2)+1):
        stack2.append(s2[j-1])
        if stack1[-1] == stack2[-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])