import sys

n = int(input())
roads = list(map(int, sys.stdin.readline().split()))
cities = list(map(int, sys.stdin.readline().split()))

res = cities[0] * roads[0]
cost = cities[0]
for i in range(1, len(cities)-1):
    cost = min(cost, cities[i])
    res += cost * roads[i]
print(res)