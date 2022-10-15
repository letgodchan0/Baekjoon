import sys
n = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
left, mid, right, res = 0, n // 2,  n-1, sys.maxsize
ans1, ans2, ans3 = 0, 0, 0

for mid in range(n):
    left = mid + 1
    right = n - 1

    while left < right:

        if abs(numbers[left] + numbers[mid] + numbers[right]) < res:
            res = abs(numbers[left] + numbers[mid] + numbers[right])
            ans1, ans2, ans3 = numbers[mid], numbers[left], numbers[right]

        if numbers[left] + numbers[mid] + numbers[right]  == 0:
            break

        elif numbers[left] + numbers[mid] + numbers[right] < 0:
            left += 1
        else:
            right -= 1

    if not res: break

print(ans1, ans2, ans3)