from collections import deque
import sys

def bfs(s, e):
    q = deque([s])
    visited = [0] * (n+1)
    visited[s] = 1
    while q:
        ns = q.popleft()
        if ns == e:
            return True

        for new in adj[ns]:
            if not visited[new]:
                q.append(new)
                visited[new] = 1
    return False

n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]
for i in range(1, n+1):
    cities = list(map(int, sys.stdin.readline().split()))
    for j in range(len(cities)):
        if cities[j]: adj[i].append(j+1)

city = list(map(int, sys.stdin.readline().split()))
check = True
for i in range(len(city)-1):
    res = bfs(city[i], city[i+1])
    if not res:
        check = False
        break
print("YES" if check else "NO")