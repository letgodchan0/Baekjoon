from collections import deque
def bfs(start, result):
    q = deque([])
    q.append(start)
    visited = [0] * 100001
    while q:
        num = q.popleft()
        if num == result:
            return visited[num]
        for check in (num+1, num-1, num*2):
            if 0 <= check <=100000 and not visited[check]:
                q.append(check)
                visited[check] = visited[num] + 1

n, m = map(int, input().split())
print(bfs(n, m))