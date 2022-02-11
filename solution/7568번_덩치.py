people = []
for _ in range(int(input())):
    people.append(list(map(int, input().split())))
cnt = 0
result =[]
while cnt < len(people):
    check = people.pop(0)
    tmp = 0
    for i in people:
        if i[0] > check[0] and i[1] > check[1]:
            tmp += 1
    result.append(tmp)
    cnt += 1
    people.append(check)
result = list(map(lambda x: x+1, result))
print(*result)