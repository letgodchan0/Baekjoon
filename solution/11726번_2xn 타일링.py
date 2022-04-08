number = int(input())
lst = [0] * 1001
lst[1], lst[2] = 1, 2
for num in range(3, number+1):
    lst[num] = lst[num-2] + lst[num - 1]
print(lst[number]%10007)