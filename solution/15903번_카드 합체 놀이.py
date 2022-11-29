import sys
n, m = map(int, input().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
cnt = 0
while cnt < m:
    small = numbers[0] + numbers[1]

    numbers[0] = small
    numbers[1] = small

    numbers.sort()
    cnt += 1

print(sum(numbers))