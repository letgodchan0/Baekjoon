n = int(input())
result = []
for _ in range(n):
    number = int(input())
    if number != 0:
        result.append(number)
    else:
        result.pop(-1)
print(sum(result))