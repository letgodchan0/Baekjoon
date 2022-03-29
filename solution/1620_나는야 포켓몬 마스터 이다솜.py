import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [input().rstrip('\n') for _ in range(n)]
atoi = {}
itoa = {}
for i in range(len(lst)):
    atoi[lst[i]] = i + 1
    itoa[i+1] = lst[i]
for _ in range(m):
    tmp = input().rstrip('\n')
    if tmp.isdigit():
        print(itoa[int(tmp)])
    else:
        print(atoi[tmp])
