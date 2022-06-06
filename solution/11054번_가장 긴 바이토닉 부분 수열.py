import sys
n = int(input())
lst = list(map(int, sys.stdin.readline().split()))

dp1 = [1] * n
dp2 = [1] * n
for i in range(1, n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp1[i] = max(dp1[i], dp1[j]+1)

for i in range(n-2, -1, -1):
    for j in range(n-1, i, -1):
        if lst[i] > lst[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)
result = []
for i in range(n):
    result.append(dp1[i]+dp2[i]-1)
print(max(result))