import sys
sys.setrecursionlimit(100000000)
def dfs(start, group):
    visited[start] = group

    for i in adj[start]:
        if not visited[i]:
            check = dfs(i, -group)
            if not check:
                return False
        elif visited[i] == visited[start]:
            return False
    return True

t = int(input())
for _ in range(t):
    v, e = map(int, input().split())
    adj = [[] for _ in range(v+1)]
    visited = [0] * (v+1)
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        adj[a].append(b)
        adj[b].append(a)

    for i in range(1, v+1):
        if not visited[i]:
            res = dfs(i, 1)
            if not res:
                break
    print("YES" if res else "NO")