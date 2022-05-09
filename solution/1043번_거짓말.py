n, m = map(int, input().split())
check = {i:0 for i in range(1, n+1)}

true_person = list(map(int, input().split()))

if true_person[0]:
    for num in true_person[1:]:
        check[num] = 1

lst = [list(map(int, input().split()))[1:] for _ in range(m)]
result = []
tmp = []
for num in lst:
    for n in num:
        if check[n]:
            result.extend(num)
            break
    tmp.append(num)

result = list(set(result))

cnt = 0
while tmp:
    ans = tmp.pop(0)
    cnt += 1
    for res in result:
        if res in ans:
            result = list(set(result + ans))
            break
    else:
        tmp.append(ans)
    if cnt > 2500:
        break

print(len(tmp))