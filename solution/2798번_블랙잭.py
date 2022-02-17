from itertools import combinations
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
answer = 0
for number in list(combinations(numbers, 3)):
    check = sum(number)
    if sum(number) <= m and check > answer:
        answer = check
print(answer)

# 시간 초과
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
answer = 0
for i in range(1,1<<len(numbers)):
    result = []
    for j in range(len(numbers)):
        if i & (1<<j):
            result.append(numbers[j])
    if len(result) != 3:
        continue
    answer = sum(result) if sum(result) > answer and sum(result) <= m else answer
print(answer)