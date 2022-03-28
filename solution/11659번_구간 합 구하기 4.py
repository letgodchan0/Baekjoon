import sys
n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

check = [0]
total = 0
for i in range(len(lst)):
    total += lst[i]
    check.append(total)

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(check[j] - check[i-1])


