N, M = map(int, input().split(' '))
board = []
for i in range(N):
    board.append(input())

result = []
for x in range(N-7):
    for y in range(M-7):
        # 각각 W와 B로 시작했을 때 변경된거 체크하기 위해서
        start_W = 0
        start_B = 0
        for i in range(x, x+8):
            for j in range(y, y+8):
                # 인덱스의 합이 짝수인 경우 색이 같아야 하고 홀수끼리도 색이 같아야함
                if (i+j) % 2 == 0:
                    if board[i][j] != 'W':
                        start_W += 1
                    if board[i][j] != 'B':
                        start_B += 1
                else:
                    if board[i][j] != 'B':
                        start_W += 1
                    if board[i][j] != 'W':
                        start_B +=1
        result.append(start_W)
        result.append(start_B)
print(min(result))