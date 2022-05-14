import sys
n = int(input())

arr = list(map(int, sys.stdin.readline().split()))
dp_max = arr; dp_min = arr

for _ in range(n-1):
    zero, one, two = map(int, sys.stdin.readline().split())

    dp_max = [zero + max(dp_max[0], dp_max[1]), one + max(dp_max[0], dp_max[1], dp_max[2]), two + max(dp_max[1], dp_max[2])]
    dp_min = [zero + min(dp_min[0], dp_min[1]), one + min(dp_min[0], dp_min[1], dp_min[2]), two + min(dp_min[1], dp_min[2])]

print(max(dp_max), min(dp_min))