import sys
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    INF = sys.maxsize
    adj = [[INF] * (n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        adj[a][b] = c
        adj[b][a] = c
    k = int(input())
    check = list(map(int, input().split()))

    for i in range(1, n+1):
        adj[i][i] = 0

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                adj[i][j] = min(adj[i][j], adj[i][k]+adj[k][j])
    res = [0] * (n+1)
    for c in check:
        res = list(map(lambda x : res[x]+adj[c][x], range(n+1)))

    print(res.index(min(res[1:])))