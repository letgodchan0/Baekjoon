n = int(input())
result = []
cnt = 0
while True:
    if n%5 == 0:
        print(n//5 + cnt)
        break
    cnt += 1
    n -= 3
    if n == 0:
        print(cnt)
        break
    if n < 3:
        print(-1)
        break