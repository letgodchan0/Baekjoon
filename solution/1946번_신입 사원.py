import sys

t = int(input())
for _ in range(t):
    n = int(input())
    lst = []
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        lst.append((a,b))

    check = sorted(lst, key = lambda x : x[0])
    cnt = 0
    people = check[0][1]
    for i in range(1, n):
        if check[i][1] < people:
            people = check[i][1]
            cnt += 1
    print(cnt + 1)