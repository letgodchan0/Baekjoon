import sys
n = int(input())
info = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    info.append((x,y))
info = info + [info[0]]

answer = 0
for i in range(n):
    x1, y1 = info[i]
    x2, y2 = info[i+1]
    answer += (x1 * y2) - (x2 * y1)

print(round(abs(answer)*0.5, 1))