from itertools import combinations
import sys

n = int(input())
numbers = []
numbers = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
numbers.sort(key=lambda x: (len(str(x)), x))

if len(numbers) > 3:
    numbers = numbers[:4]

numbers = list(combinations(numbers, 2))
check = []
for num1, num2 in numbers:
    check.append(int(str(num1)+str(num2)))
    check.append(int(str(num2)+str(num1)))

check.sort()
print(check[2])