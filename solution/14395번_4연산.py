from collections import deque

def bfs():
    q = deque([(s, '')])
    check = set()
    check.add(s)
    while q:
        num, res = q.popleft()

        if num == t:
            return res

        for code in ['*', '+', '-', '/']:
            if code == '*':
                next = num * num
            elif code == '+':
                next = num + num
            elif code == '-':
                next = num - num
            else:
                if num:next = num // num
            if next not in check and next <= max(s, t):
                q.append((next, res + code))
                check.add(next)

    return -1

s, t = map(int, input().split())

answer = bfs()
if answer == '':
    print(0)
else:
    print(answer)