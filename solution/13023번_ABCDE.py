import sys

def dfs(start, depth):
    global check
    visited[start] = 1

    if depth == 4:
        check = True
        return

    for num in adj[start]:
        if not visited[num]:
            dfs(num, depth + 1)
            visited[num] = 0

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
visited = [0 for _ in range(n)]
check = False
for _ in range(m):
    first, second = map(int, sys.stdin.readline().split())
    adj[first].append(second)
    adj[second].append(first)

for i in range(n):
    dfs(i, 0)
    visited[i] = 0
    if check:
        break
print(1 if check else 0)
