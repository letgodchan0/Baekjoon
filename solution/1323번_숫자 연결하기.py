# 1번 방법
n, k = map(int, input().split())

v = [0] * k
cnt = 1
res = n
while True:
    tmp = n % k
    if not tmp:
        print(cnt)
        break
    else:
        if v[tmp]:
            print(-1)
            break
        else:
            cnt += 1
            n = int(str(tmp) + str(res))
            v[tmp] = 1

# 2번 방법
n, k = map(int, input().split())

v = [0] * k
x = 10**len(str(n))
cnt = 1
res = n
while True:
    tmp = n % k
    if not tmp:
        print(cnt)
        break
    else:
        if v[tmp]:
            print(-1)
            break
        else:
            cnt += 1
            n = tmp*x + res
            v[tmp] = 1