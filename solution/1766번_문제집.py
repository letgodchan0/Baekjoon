import sys, heapq
n, m = map(int, input().split())
outdegree = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    outdegree[a].append(b)
    indegree[b] += 1

order = []
heap = []
for i in range(1, n+1):
    if not indegree[i]:
        heap.append(i)

while heap:
    level = heapq.heappop(heap)
    print(level, end=' ')
    for i in outdegree[level]:
        indegree[i] -= 1
        if not indegree[i]:
            heapq.heappush(heap, i)