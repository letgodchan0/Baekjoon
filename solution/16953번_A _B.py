from collections import deque

def bfs(a, time):
    q = deque([])
    q.append((a, time))
    while q:
        number, cnt = q.popleft()
        if number == b:
            return cnt + 1

        if number * 2 <= b:
            q.append((number * 2, cnt + 1))

        if int(str(number) + '1') <= b:
            q.append((int(str(number) + '1'), cnt + 1))

    return -1

a, b = map(int, input().split())
print(bfs(a, 0))