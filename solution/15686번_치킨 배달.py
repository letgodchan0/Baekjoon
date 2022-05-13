import sys
from itertools import combinations

n, m = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
chicken = []
house = []
ans = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            chicken.append((i,j))
        elif arr[i][j] == 1:
            house.append((i,j))

chicken_house = list(combinations(chicken, m))
lst = []

for chicken in chicken_house:
    ans = 0
    for i,j in house:
        distance = 101
        for x,y in chicken:
            tmp = abs(x-i) + abs(y-j)
            if distance > tmp:
                distance = tmp
        ans += distance
    lst.append(ans)
print(min(lst))
