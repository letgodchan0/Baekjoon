from collections import deque
def bfs(num):
    q = deque([])
    q.append((num, 0))
    visited = [0] * 100001
    visited[num] = 1
    while q:
        number, time = q.popleft()
        if number == k:
            return time

        for i in (2 * number, number - 1, number + 1):
            if 0 <= i < 100001 and not visited[i]:
                visited[i] = 1
                if i == 2 * number:
                    q.append((i, time))
                else:
                    q.append((i,time+1))

n, k = map(int, input().split())

print(bfs(n))