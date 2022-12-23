import sys
sys.setrecursionlimit(10000)

def dfs(start):
    global cnt
    for node in sorted(adj[start]):
        if not visited[node]:
            cnt += 1
            visited[node] = cnt
            dfs(node)

n, m, r = map(int, input().split())
adj = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
visited[r], cnt = 1, 1
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

dfs(r)
for i in range(1, n+1):
    print(visited[i])