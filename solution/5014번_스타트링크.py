# 저 이고 8월 15일에 풀었습니다 ㅜ
from collections import deque

def bfs(start):
    q = deque([])
    q.append((start, 0))
    visited = [0] * (f+1)
    visited[start] = 1
    while q:
        res, cnt = q.popleft()
        if res == g:
            return cnt
        for x in ('u', 'd'):
            new = res + u if x == 'u' else res - d
            if 1 <= new <= f and not visited[new]:
                q.append((new, cnt + 1))
                visited[new] = 1
    return "use the stairs"
f, s, g, u, d = map(int, input().split())
print(bfs(s))