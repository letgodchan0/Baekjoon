from collections import deque
def bfs():
    q = deque([1])
    visited[1] = 1
    cnt = 0
    while q:
        v = q.popleft()
        for i in lst[v]:
            if not visited[i] and i != 0:
                visited[i] = 1
                q.append(i)
                cnt += 1
    return cnt


computer = int(input())
n = int(input())
lst = [[0]] * (computer+1)

visited = [0] * (computer+1)
for _ in range(n):
    idx, val = map(int, input().split())
    if lst[idx] == [0]:
        lst[idx] = [val]
    else:
        lst[idx] = lst[idx] + [val]
    if lst[val] == [0]:
        lst[val] = [idx]
    else:
        lst[val] = lst[val] + [idx]

print(bfs())
