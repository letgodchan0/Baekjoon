from collections import deque
def bfs(n):
    q = deque([])
    q.append((n,[n]))
    res, ans = 50, []
    visited = [0] * (n + 1)
    visited[n] = 1
    while q:
        num, lst = q.popleft()

        if num == 1:
            if res > len(lst):
                res = len(lst)
                ans = [] + lst

        if len(lst) > res or num < 1:
            continue

        new_num = 0
        if not num % 3 and not visited[num//3]:
            new_num = num // 3
            visited[num//3] = 1
            q.append((new_num, lst + [new_num]))
        if not num % 2 and not visited[num//2]:
            new_num = num // 2
            visited[num//2] = 1
            q.append((new_num, lst + [new_num]))
        if not visited[num-1]:
            q.append((num-1, lst + [num-1]))
            visited[num-1] = 1

    return ans
n = int(input())
res = bfs(n)
print(len(res)-1)
print(*res)