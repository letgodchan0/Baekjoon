import sys

n, k = map(int, input().split())
numbers = list(map(int, sys.stdin.readline().split()))

res = []
for i in range(n-1):
    res.append(numbers[i+1] - numbers[i])

res.sort()
print(sum(res[:n-k]))