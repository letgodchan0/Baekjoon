import sys
input = sys.stdin.readline

def bf(start):
    d = [INF] * (n + 1)
    d[start] = 0
    for i in range(n):
        for s, e, t in adj:
            if d[e] > d[s] + t:
                d[e] = d[s] + t
                if i == n - 1:
                    return True
    return False

t = int(input())
for _ in range(t):
    n, m, w = map(int, input().split())
    INF = sys.maxsize
    adj = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        adj.append((s, e, t))
        adj.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        adj.append((s, e, -t))
    if bf(1):
        print('YES')
    else:
        print('NO')
