n = int(input())

last = 666
cnt = 0

while True:
    if '666' in str(last):
        cnt += 1
    if cnt == n:
        print(last)
        break
    last += 1