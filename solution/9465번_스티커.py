t = int(input())
for _ in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0, 0] for _ in range(n+1)]

    # 위쪽 스티커 선택
    dp[1][0] = arr[0][0]
    # 아래 스티커 선택
    dp[1][1] = arr[1][0]

    for i in range(2, n+1):
        # 위쪽 스티커 선택
        dp[i][0] = max(dp[i-2][1], dp[i-1][1]) + arr[0][i-1]

        # 아래 스티커 선택
        dp[i][1] = max(dp[i-2][0], dp[i-1][0]) + arr[1][i-1]

    print(max(dp[n]))

