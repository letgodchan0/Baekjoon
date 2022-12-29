from collections import deque
import sys

def bfs():
    q = deque([(1, 0)])
    visited = [0 for _ in range(n+1)]
    visited[1] = 1
    answer = -1
    while q:
        friend, cnt = q.popleft()

        if cnt > 2:continue
        else:answer += 1

        for new in adj[friend]:
            if not visited[new]:
                q.append((new, cnt+1))
                visited[new] = 1
    return answer


n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)

print(bfs())