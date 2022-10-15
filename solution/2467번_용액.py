import sys
n = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
left, right, res = 0, n-1, sys.maxsize
ans1, ans2 = 0, 0

while left < right:
    if abs(numbers[left] + numbers[right]) < res:
        res = abs(numbers[left] + numbers[right])
        ans1, ans2 = numbers[left], numbers[right]

    if numbers[left] + numbers[right] < 0:
        left += 1
    else:
        right -= 1

print(ans1, ans2)