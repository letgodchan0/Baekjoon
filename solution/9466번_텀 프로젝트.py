import sys
sys.setrecursionlimit(10000000)

def dfs(start):
    global res
    visited[start] = 1
    check.append(start)
    new = students[start]

    if visited[new]:
        if new in check:
            res += check[check.index(new):]
        return
    else:
        dfs(new)

t = int(input())
for _ in range(t):
    n = int(input())
    students = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [0 for _ in range(n+1)]
    res = []
    for i in range(1, n+1):
        if not visited[i]:
            check = []
            dfs(i)

    print(n - len(res))


""" 82% 시간초과
import sys
sys.setrecursionlimit(10000000)

def dfs(start, cnt):
    global i

    if cnt > 0 and start == i:
        return True

    if not visited[start]:
        visited[start] = 1
        check = dfs(students[start], cnt + 1)
        if not check:
            visited[start] = 0
        else:
            return True

t = int(input())
for _ in range(t):
    n = int(input())
    students = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        dfs(i, 0)

    print(visited.count(0) - 1)
"""