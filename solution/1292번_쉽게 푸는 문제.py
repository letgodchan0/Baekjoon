n, m = map(int, input().split())
num = 1
lst = [0]
while True:
    for i in range(1, num+1):
        lst.append(num)
    num += 1
    if len(lst) >= 1001:
        break

for i in range(1, m+1):
    lst[i] += lst[i-1]

print(lst[m]-lst[n-1])