n = int(input())
cnt = 1
check = []
stack = []
result = True
for _ in range(n):
    number = int(input())
    while cnt <= number:
        stack.append('+')
        check.append(cnt)
        cnt += 1
    if check[-1] == number:
        stack.append('-')
        check.pop()
    else:
        result = False
if not result:
    print('NO')
else:
    for i in stack:
        print(i)



# 틀린 이유 아직 못찾은 코드
# n = int(input())
# arr = [int(input()) for _ in range(n)]

# def solution(arr):
#     stack = ['+'] * arr[0]
#     last_number = arr[0]
#     for i in range(len(arr)):
#         if last_number >= arr[i]:
#             stack.append('-')
#             if arr[i] != arr[-1] and arr[i] < arr[i+1] < last_number:
#                 stack = []
#                 return stack
#         else:
#             stack +=  ['+'] * (arr[i] - last_number)
#             last_number = arr[i]
#             stack.append('-')
#     return stack
# result = solution(arr)
# if not result:
#     print('NO')
# else:
#     for i in result:
#         print(i)