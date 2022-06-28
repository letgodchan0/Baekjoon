import sys
from collections import deque

def bfs(num):
    q = deque([])
    q.append((num, 0))
    visited = [0] * 100001
    visited[num] = 1
    while q:
        number, time = q.popleft()
        if number == k:
            return time

        for i in (2 * number, number - 1, number + 1):
            if 0 <= i < 100001 and not visited[i]:
                visited[i] = 1
                q.append((i, time+1))
                check[i] = number

n, k = map(int, sys.stdin.readline().split())
check = [0] * 100001
time = bfs(n)
print(time)
lst = []
tmp = k
for _ in range(time+1):
    lst.append(tmp)
    tmp = check[tmp]
print(*lst[::-1])