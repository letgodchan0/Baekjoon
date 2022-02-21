import sys
n = int(input())
check = []
for _ in range(n):
    person = sys.stdin.readline().split()
    check.append([int(person[0]), person[1]])
check = sorted(check, key = lambda x: x[0])
for i in check:
    print(*i)