n = int(input())

total = 1
for num in range(2, n+1):
    total *= num
number = str(total)[::-1]
cnt = 0
for i in number:
    if i != '0':
        break
    cnt += 1
print(cnt)