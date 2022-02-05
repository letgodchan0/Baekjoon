n = int(input())
numbers = list(range(1, n+1))

while True:
    if len(numbers) == 1:
        print(numbers[0])
        break
    # 길이가 홀수면 0번째 제거, 1번째 맨뒤로
    if len(numbers) % 2:
        numbers.pop(0)
        numbers.append(numbers.pop(0))
    else:
        numbers = [numbers[i] for i in range(len(numbers)) if i % 2]



# 시간 초과
# n = int(input())

# numbers = list(range(1, n+1))
# while True:
#     numbers.pop(0)
#     numbers.append(numbers.pop(0))
#     if len(numbers) == 1:
#         print(numbers[0])
#         break