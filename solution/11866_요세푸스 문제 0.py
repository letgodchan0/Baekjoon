n, k = map(int, input().split())
numbers = list(range(1, n+1))
lst = []
cnt = 0
idx = -1

while True:
    idx = 0 if idx == n-1 else idx+1
    if numbers[idx] not in lst:
        cnt += 1
    else:
        continue
    if cnt == k:
        lst.append(numbers[idx])
        cnt = 0
    if len(lst) == n:
        break

print('<', end='')
for i in range(len(lst)):
    print(lst[i], end='')
    if i != n-1:
        print(',', end=' ')
    else:
        print('>')