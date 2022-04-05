import sys
n = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
lst = list(set(numbers))
lst.sort()
result = {}
for i in range(len(lst)):
    result[lst[i]] = i

for num in numbers:
    print(result[num], end = ' ')