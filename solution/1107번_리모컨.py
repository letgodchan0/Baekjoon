import sys
n = int(input())
m = int(input())
lst = list(map(int, sys.stdin.readline().split()))
answer = abs(100 - n)
for number in range(999895):
    num = str(number)
    for i in range(len(num)):
        if int(num[i]) in lst:
            break
        elif i == len(num) - 1:
            answer = min(answer, abs(int(num)-n)+len(num))
print(answer)