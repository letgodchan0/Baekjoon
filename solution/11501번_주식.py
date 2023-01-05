import sys

t = int(input())
for _ in range(t):
    n = int(input())
    numbers = list(map(int, sys.stdin.readline().split()))
    cnt, cost, profit, check = 0, 0, 0, numbers[-1]

    for i in range(n-2, 0, -1):
        if numbers[i] < check:
            cnt += 1
            cost += numbers[i]
        else:
            profit += cnt * check - cost
            cost, cnt, check = 0, 0, numbers[i]

    if numbers[0] < check:
        cnt += 1
        cost += numbers[0]
    profit += cnt * check - cost

    print(profit)