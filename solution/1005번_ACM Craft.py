from collections import deque
import sys

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    time = [0] + list(map(int, sys.stdin.readline().split()))
    outegree = [[] for _ in range(n+1)]
    check = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    for _ in range(k):
        In, Out = map(int, sys.stdin.readline().split())
        outegree[In].append(Out)
        check[Out].append(In)
        indegree[Out] += 1
    end = int(input())

    q = deque([])
    for i in range(1, n+1):
        if not indegree[i]:
            q.append(i)
    dp = [0] * (n+1)
    while q:
        node = q.popleft()
        max_time = 0
        for before_node in check[node]:
            max_time = max(max_time, dp[before_node])

        dp[node] = time[node] + max_time

        if node == end:
            print(dp[end])

        for next_node in outegree[node]:
            indegree[next_node] -= 1
            if not indegree[next_node]:
                q.append(next_node)