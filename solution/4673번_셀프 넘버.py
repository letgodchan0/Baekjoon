def check(n):
    n = n + sum(map(int, str(n)))
    return n

tmp = set()
for i in range(1, 10001):
    tmp.add(check(i))

for i in range(1, 10001):
    if i not in tmp:
        print(i)