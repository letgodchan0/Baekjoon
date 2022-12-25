numbers = input()

start = int(numbers[0])
check = {}
check[start] = 1
for num in numbers:
    if int(num) != start:
        start = (start - 1) * -1
        check[start] = check.get(start, 0) + 1

print(min(check.get(0, 0), check.get(1, 0)))