import sys

def find(x, y):
    color = indices[x][y]
    # 좌표 기준으로 양쪽 확인
    for dx, dy, ddx, ddy in [(-1,0,1,0),(0,-1,0,1),(-1,-1,1,1),(-1,1,1,-1)]:
        nx, ny = x + dx, y + dy
        
        # 세로일 때 제일 윗줄 체크해주려고
        res = [(x, y)]
        while 0 <= nx < 19 and 0 <= ny < 19 and indices[nx][ny] == color:
            res.append((nx,ny))
            nx, ny = nx + dx, ny + dy

        nnx, nny = x + ddx, y + ddy

        while 0 <= nnx < 19 and 0 <= nny < 19 and indices[nnx][nny] == color:
            res.append((nnx,nny))
            nnx, nny = nnx + ddx, nny + ddy

        # 5개일 때만 체크
        total = len(res)
        res.sort(key = lambda x : x[0])
        if total == 5:
            # 가로
            if dy == 0 and ddy == 0:
                return res[0]
            else:
                return (x,y)

    return (-1,-1)

indices = [list(map(int, sys.stdin.readline().split())) for _ in range(19)]

check = False
for i in range(19):
    for j in range(19):
        # 왼쪽부터 탐색하기
        if indices[j][i]:
            a, b = find(j, i)
            # check로 분기 처리하면서, 5목이 완성될 때 다른 경우 체크 x
            if a >=0 and b >=0 and not check:
                check = True
                print(indices[j][i])
                print(a+1, b+1)
if not check:
    print(0)