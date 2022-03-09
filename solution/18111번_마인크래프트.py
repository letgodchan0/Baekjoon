n, m , block = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
counts = []

for i in lst:
    counts.extend(i)
min_v, max_v = min(counts), max(counts)

answer = []
for num in range(min_v, max_v+1):
    time = 0
    inv = block
    for i in range(n):
        for j in range(m):
            if lst[i][j] > num:
                time += (lst[i][j]-num)*2
                inv += lst[i][j] - num
            else:
                time += num-lst[i][j]
                inv -= num-lst[i][j]
    if inv >= 0:
        answer.append([time, num])
answer.sort(key=lambda x :(x[0], -x[1]))
print(*answer[0])