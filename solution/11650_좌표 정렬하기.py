n = int(input())
numbers = []
for _ in range(n):
    numbers.append(tuple(map(int,input().split())))
numbers = sorted(numbers, key = lambda x: (x[0],x[1]))
for number in numbers:
    print(*number)