import sys

N, M, x, y, K = map(int, sys.stdin.readline().split())
indices = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
order = list(map(int, sys.stdin.readline().split()))
dice = {i : 0 for i in range(1, 7)}
check = [[0] * 3 for _ in range(4)]
check[0][1], check[1][1], check[2][1], check[3][1], check[1][0], check[1][2] = 2, 1, 5, 6, 4, 3

top, bottom = dice[check[1][1]], dice[check[3][1]]
cnt = 1
for o in order:
    a, b = top, bottom
    if o == 1:  # 동쪽
        nx, ny = x, y+1
        # 바깥으로 이동하는 경우 무시
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            top, bottom = a, b
            continue
        check[1][0], check[1][1], check[1][2], check[3][1] = check[3][1], check[1][0], check[1][1], check[1][2]
    elif o == 2: # 서쪽
        # 바깥으로 이동하는 경우 무시
        nx, ny = x, y-1
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            top, bottom = a, b
            continue
        check[1][0], check[1][1], check[1][2], check[3][1] = check[1][1], check[1][2], check[3][1], check[1][0]
    elif o == 3: # 북쪽
        # 바깥으로 이동하는 경우 무시
        nx, ny = x-1, y
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            top, bottom = a, b
            continue
        check[0][1], check[1][1], check[2][1], check[3][1] = check[1][1], check[2][1], check[3][1], check[0][1]
    else:   # 남쪽
        nx, ny = x+1, y
        # 바깥으로 이동하는 경우 무시
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            top, bottom = a, b
            continue
        check[0][1], check[1][1], check[2][1], check[3][1] = check[3][1], check[0][1], check[1][1], check[2][1]

    top = check[1][1]
    bottom = check[3][1]
    print(dice[top])

    # 지도의 값이 0이 아닐 때
    if indices[nx][ny]:
        dice[bottom] = indices[nx][ny]
        indices[nx][ny] = 0

    # 지도의 값이 0이라면
    else:
        indices[nx][ny] = dice[bottom]

    # 좌표 변경
    x, y = nx, ny