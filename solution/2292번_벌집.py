n = int(input())

r = 0
check = 1
while check <= n:
    if n == 1:
        print(1)
        break
    check += 6*r
    if n <= check:
        print(r+1)
        break
    r += 1