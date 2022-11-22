n, m = map(int, input().split())
numbers = list(map(int, input().split()))
neg, pos = [], []

for number in numbers:
    if number > 0:
        pos.append(number)
    else:
        neg.append(number)
neg.sort()
pos.sort(reverse =  True)

check = []
for i in range(len(neg) // m):
    check.append(abs(neg[m*i]))

if len(neg) % m:
    check.append(abs(neg[(len(neg)//m)*m]))

for i in range(len(pos) // m):
    check.append(pos[m*i])

if len(pos) % m:
    check.append(pos[(len(pos)//m)*m])

check.sort()
answer = check[-1] + 2 * sum(check[:-1])
print(answer)