from collections import deque
import sys

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if not num % i:
            return False
    return True

def check(num1, num2):
    num1, num2 = str(num1), str(num2)
    cnt = 0
    for i in range(4):
        if num1[i] != num2[i]:
            cnt += 1
    return True if cnt == 1 else False

def bfs(start):
    q = deque([])
    q.append((start, 0))
    visited = [0] * 9000
    visited[start-1000] = 1
    lst = list(range(1, 10)) + list(range(10, 100, 10)) + list(range(100, 1000, 100)) + list(range(1000, 10000, 1000)) + list(range(-1, -10, -1)) + list(range(-10, -100, -10)) + list(range(-100, -1000, -100)) + list(range(-1000, -10000, -1000))
    while q:
        current, cnt = q.popleft()
        if current == end:
            return cnt

        for add in lst:
            prime_number = current + add
            if 1000 <= prime_number < 10000 and not visited[prime_number-1000] and isPrime(prime_number) and check(current, prime_number):
                q.append((prime_number, cnt + 1))
                visited[prime_number-1000] = 1

    return "Impossible"

t = int(input())
for _ in range(t):
    start, end = map(int, sys.stdin.readline().split())
    print(bfs(start))