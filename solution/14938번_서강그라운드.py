import sys

n, m, r = map(int, input().split())
lst = list(map(int, input().split()))
INF = int(1e9)
adj = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    adj[i][i] = 0

for _ in range(r):
    u, v, w = map(int, sys.stdin.readline().split())
    adj[u][v] = adj[v][u] = w


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])

answer = 0
for i in range(1, n+1):
    tmp = 0
    for j in range(1, n+1):
        if adj[i][j] <= m:
            tmp += lst[j-1]
    if tmp > answer:
        answer = tmp
print(answer)
