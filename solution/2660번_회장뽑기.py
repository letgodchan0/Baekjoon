from collections import deque
import sys

def bfs(num):
    q = deque([(num,0)])
    visited = [0] * (n+1)
    visited[num] = 1
    res = 0
    while q:
        number, cnt = q.popleft()
        res = max(res, cnt)
        for new in adj[number]:
            if not visited[new]:
                q.append((new, cnt + 1))
                visited[new] = 1
    return res

n = int(input())
adj = [[] for _ in range(n+1)]
check = [0] * (n+1)
while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1 :
        break
    adj[a].append(b)
    adj[b].append(a)

for i in range(1, n+1):
    check[i] = bfs(i)

check = check[1:]

print(min(check), check.count(min(check)))
for i in range(len(check)):
    if check[i] == min(check):
        print(i+1, end = " ")