from collections import deque
import sys
def D(n):
    if 2 * n > 9999:
        return (2 * n) % 10000
    else:
        return 2 * n
def S(n):
    if n > 0:
        return n - 1
    else:
        return 9999
def L(n):
    num1 = n % 1000
    num2 = n // 1000
    return 10 * num1 + num2
def R(n):
    num1 = n // 10
    num2 = n % 10
    return 1000 * num2 + num1

def bfs(a, b):
    q = deque([])
    q.append((a, ''))
    visited = [0] * 10000
    visited[a] = 1
    while q:
        num, answer = q.popleft()
        if num == b:
            return answer
        for ni, nj in [(D(num), 'D'), (S(num), 'S'), (L(num), 'L'), (R(num), 'R')]:
            if 0 <= ni < 10000 and not visited[ni]:
                q.append((ni, answer + nj))
                visited[ni] = 1

T = int(input())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(bfs(a, b))