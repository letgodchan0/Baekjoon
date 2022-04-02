from collections import deque
import sys
def bfs(start):
    q = deque([])
    visited = [0] * (v+1)
    q.append(start)
    visited[start] = 1
    while q:
        n = q.popleft()
        for w in adj[n]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[n] + 1
    answer = max(visited)
    idx = len(visited)
    cnt = 0
    for i in range(len(visited)):
        if visited[i] == answer:
            cnt += 1
            if idx > i:
                idx = i
    return idx, answer-1, cnt

v, e = map(int, sys.stdin.readline().split())
arr = []
for _ in range(e):
    arr.extend(map(int, sys.stdin.readline().split()))
adj = [[] for _ in range(v+1)]

for i in range(e):
    n1, n2 = arr[i*2], arr[i*2+1]
    adj[n1].append(n2)
    adj[n2].append(n1)

print(*bfs(1))

