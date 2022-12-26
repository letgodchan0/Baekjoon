n, m = map(int, input().split())
pac, per = [], []
for _ in range(m):
    a, b = map(int, input().split())
    pac.append(a);per.append(b)

min_pac = min(pac)
min_per = min(per)

if n <= 6:
    if min_per * n < min_pac:print(min_per * n)
    else:print(min_pac)
else:
    if min_per * 6 < min_pac:print(min_per * n)
    else:
        check = n % 6
        mok = n // 6
        if check * min_per < min_pac:print(mok * min_pac + check * min_per)
        else:print((mok+1) * min_pac)