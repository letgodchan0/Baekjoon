from collections import deque
import sys

def move(lst, direction):
    # 시계 방향이라면
    if direction == 1:return [lst[7]] + lst[:7]
    # 반 시계
    else:return lst[1:] + [lst[0]]

indices = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(4)]
check = [[1], [0,2], [1,3], [2]]
K = int(input())

for k in range(K):
    num, way = map(int, sys.stdin.readline().split())
    num -= 1
    visited = [0 for _ in range(4)]
    visited[num] = 1
    q = deque([(num, way)])
    order = [(num, way)]

    while q:
        node, new = q.popleft()
        for c in check[node]:
            if node == 1 or node == 2:
                if indices[node][6] != indices[node-1][2]:
                    if not visited[node-1]:
                        q.append((node-1, new*-1))
                        visited[node-1] = 1
                        order.append((node-1, new*-1))

                if indices[node][2] != indices[node+1][6]:
                    if not visited[node+1]:
                        q.append((node+1, new*-1))
                        visited[node+1] = 1
                        order.append((node+1, new*-1))
            else:
                if not node:
                    if indices[node][2] != indices[node+1][6]:
                        if not visited[node+1]:
                            q.append((node+1, new*-1))
                            visited[node + 1] = 1
                            order.append((node + 1, new * -1))
                else:
                    if indices[node][6] != indices[node-1][2]:
                        if not visited[node - 1]:
                            q.append((node-1, new*-1))
                            visited[node - 1] = 1
                            order.append((node - 1, new * -1))

    for i, direction in order:
        indices[i] = move(indices[i], direction)

total, cnt = 0, 1
for i in range(4):
    if indices[i][0]:
        total += 1 * cnt
    cnt *= 2

print(total)