lst = list(input())
lst.sort()
res = ''
for num in lst:
    res = num + res
print(res)