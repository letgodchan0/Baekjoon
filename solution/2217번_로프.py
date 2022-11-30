n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort()
check, length = [], len(lst)

for i in range(len(lst)):
    check.append(lst[i] * length)
    length -= 1

print(max(check))