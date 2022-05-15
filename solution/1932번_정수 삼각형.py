import sys
n = int(input())
if n == 1:
    print(int(input()))
else:
    dp = [0] * n
    first = int(input())
    sec1, sec2 = map(int, input().split())
    dp[0] = sec1 + first; dp[1] = sec2 + first

    for _ in range(n-2):
        tmp = list(map(int, sys.stdin.readline().split()))
        check = dp.copy()
        dp[0] += tmp[0]; dp[len(tmp)-1] = tmp[-1] + dp[len(tmp)-2]

        for i in range(1, len(tmp)-1):
            dp[i] = tmp[i] + max(check[i-1], check[i])
    print(max(dp))
