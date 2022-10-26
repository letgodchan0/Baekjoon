n = int(input())
check = {}
for _ in range(n):
    a = input()
    check[a] = check.get(a, 0) + 1

lst = sorted(check.keys(), key=lambda x: (-check[x], x))
print(lst[0])