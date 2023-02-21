from collections import deque
import sys

N = int(input())
indices = [[0] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]
K = int(input())
for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    indices[x-1][y-1] = 1

L = int(input())
direction = {}
for _ in range(L):
    x, c = sys.stdin.readline().split()
    direction[int(x)] = c

q = deque([(deque([(0,0)]),0,"r")])
while q:
    snake, cnt, way = q.popleft()

    # 시간 증가
    cnt += 1

    # 뱀 머리 좌표
    x, y = snake[0]

    # 몸 길이 늘리기
    if way == 'r':
        nx, ny = x, y + 1
    elif way == 'l':
        nx, ny = x, y - 1
    elif way == 'd':
        nx, ny = x + 1, y
    else:
        nx, ny = x - 1, y

    if nx < 0 or nx >= N or ny < 0 or ny >= N or (nx, ny) in snake:
        print(cnt)
        break

    # 사과가 있다면,
    if indices[nx][ny]:
        indices[nx][ny] = 0

    # 사과가 없다면 꼬리 좌표 제거
    else:
        snake.pop()

    # 새로운 뱀 머리 위치 다시 넣어주기
    snake.appendleft((nx, ny))

    # 방향 전환
    if direction.get(cnt):
        val = direction[cnt]

        if way == 'r':
            if val == 'L': way = 'u'
            else: way = 'd'

        elif way == 'l':
            if val == 'L': way = 'd'
            else: way = 'u'

        elif way == 'd':
            if val == 'L': way = 'r'
            else: way = 'l'

        else:
            if val == 'L': way = 'l'
            else: way = 'r'

    q.append((snake, cnt, way))