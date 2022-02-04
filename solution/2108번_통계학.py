import sys
n = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(n)]
numbers.sort()
print(round(sum(numbers)/n))
print(numbers[int((n-1)/2)])

def many(number):
    numbers = {}
    for num in number:
        numbers[num] = numbers.get(num, 0) + 1

    max_number = max(numbers.values())
    result = []
    for num in numbers.keys():
        if numbers[num] == max_number and num not in result:
            result.append(num)
    if len(result) == 1:
        return result[0]
    else:
        return sorted(result, reverse=True)[-2]
print(many(numbers))
print(numbers[-1]-numbers[0])