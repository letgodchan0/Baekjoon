from collections import deque

def bfs(start):
    q = deque([])
    q.append(start)
    visited = [0] * (n+1)
    while q:
        check = q.popleft()
        for i in adj[check]:
            if not visited[i]:
                visited[i] = visited[check] + 1
                q.append(i)
    return visited

n = int(input())
s1, s2 = map(int, input().split())
m = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

res = bfs(s1)
print(res[s2] if res[s2] > 0 else -1)