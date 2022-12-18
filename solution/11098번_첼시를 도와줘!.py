t = int(input())

for _ in range(t):
    n = int(input())
    cnt, name = -1, ""
    for _ in range(n):
        info = input().split()
        if int(info[0]) > cnt:
            cnt = int(info[0])
            name = info[1]
    print(name)