from collections import deque
def bfs(start):
    q = deque([])
    q.append(start)
    while q:
        v = q.popleft()
        for i in lst[v]:
            visited[i] = 1
            q.append(i)
        lst[v] = [0]

n = int(input())
arr = list(map(int, input().split()))
delete = int(input())
lst = [[] for _ in range(n)]
visited = [0] * n
for i in range(n):
    if arr[i] >= 0:
        lst[arr[i]].append(i)
bfs(delete)
cnt = 0

for i in lst:
    if not i:
        cnt += 1
if arr[delete] != -1 and len(lst[arr[delete]]) == 1:
    cnt += 1
print(cnt)