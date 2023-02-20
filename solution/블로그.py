import sys

n, x = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    numbers[i] += numbers[i-1]

numbers = [0] + numbers
start = x
check = {}
for i in range(start, n+1):
    val = numbers[i] - numbers[i - x]
    check[val] = check.get(val, 0) + 1

max_val = max(check.keys())
if max_val:
    print(max_val)
    print(check.get(max_val))
else:
    print('SAD')