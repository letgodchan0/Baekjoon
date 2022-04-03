from collections import deque
import sys
n, m = map(int, input().split())
arr = []
for _ in range(m):
    arr.extend(list(map(int, sys.stdin.readline().split())))

lst = [[] for _ in range(n+1)]

for i in range(m):
    n1, n2 = arr[i*2], arr[i*2+1]
    lst[n1].append(n2)
    lst[n2].append(n1)

visited = [0] * (n+1)
q = deque([])
cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        cnt += 1
        q.append(i)
        visited[i] = cnt
        while q:
            idx = q.popleft()
            for num in lst[idx]:
                if not visited[num]:
                    visited[num] = cnt
                    q.append(num)
print(max(visited))


