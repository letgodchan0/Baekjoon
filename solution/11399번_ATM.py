n = int(input())
lst = list(map(int, input().split()))
lst.sort()
total = 0
answer = 0
for i in lst:
    total += i
    answer += total
print(answer)