def total(number):
    return sum(map(int, str(number)))
n = int(input())
cnt = 0
while cnt < n:
    if cnt + total(cnt) == n:
        print(cnt)
        break
    cnt += 1
if cnt == n:
    print(0)