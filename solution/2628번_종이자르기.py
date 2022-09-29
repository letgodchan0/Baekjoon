width, height = map(int, input().split())

lst = [[0], [0]]
n = int(input())
for i in range(n):
    cut_direction, idx = map(int, input().split())
    lst[cut_direction].append(idx)

lst[0].append(height); lst[1].append(width)
lst[0].sort(); lst[1].sort()

max_height, max_width = 0, 0

for idx in range(1, len(lst[0])):
    h = lst[0][idx] - lst[0][idx - 1]
    if max_height < h:
        max_height = h

for idx in range(1, len(lst[1])):
    w = lst[1][idx] - lst[1][idx - 1]
    if max_width < w:
        max_width = w

print(max_height * max_width)
