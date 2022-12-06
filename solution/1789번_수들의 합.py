s = int(input())

n, check, cnt = 0, 0, 0
while check < s:
    check += n
    n += 1
    cnt += 1

print(n-1)