from collections import deque
import sys

def bfs():
    q = deque([(0,1)])
    visited = [0] * n
    visited[0] = 1
    visited_hyper = [0] * m
    while q:
        station, cnt = q.popleft()

        check = []
        for i in stations[station]:
            if not visited_hyper[i]:
                check.append(i)
                visited_hyper[i] = 1

        for hyper in check:
            for i in hyper_tube[hyper]:
                if not visited[i]:
                    if i == n - 1:
                        return cnt + 1
                    visited[i] = 1
                    q.append((i, cnt+1))
    return -1

n, k, m = map(int, input().split())
stations = [[] for _ in range(n)]
hyper_tube = [[] for _ in range(m)]

for i in range(m):
    numbers = list(map(int, sys.stdin.readline().split()))
    for num in numbers:
        hyper_tube[i].append(num - 1)
        stations[num - 1].append(i)

if n == 1: print(1)
else: print(bfs())