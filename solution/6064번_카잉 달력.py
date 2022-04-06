t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())
    while x <= m*n:
        if not (x-y)%n:
            print(x)
            break
        x += m
    else:
        print(-1)