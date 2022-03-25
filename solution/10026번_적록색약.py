# 그냥 한번에 다 도는건데 왜 틀리는지 모르겠음...
# def bfs(i, j, color):
#     tmp = 0  # 적록 색약
#     q = []
#     q.append((i,j))
#     while q:
#         i, j = q.pop(0)
#         for di, dj in [[-1,0], [1,0], [0,-1], [0,1]]:
#             ni, nj = i + di, j + dj
#             # 적록 색약
#             if 0 <= ni < n and 0 <= nj < n and visited[ni][nj][1] == 0:
#                 tmp = 1
#                 if (color == 'R' or color == 'G') and (arr[ni][nj] == 'R' or arr[ni][nj] == 'G'):
#                     visited[ni][nj][1] = color
#                     q.append((ni, nj))
#                 elif arr[ni][nj] == color:
#                     visited[ni][nj][1] = color
#                     q.append((ni, nj))
#             # 일반 사람
#             if 0 <= ni < n and 0 <= nj < n and visited[ni][nj][0] == 0 and arr[ni][nj] == color and arr[i][j] == color:
#                 visited[ni][nj][0] = color
#                 q.append((ni, nj))
#     return 1, tmp

# n = int(input())
# arr = [list(input()) for _ in range(n)]
# visited = [[[0]*2 for _ in range(n)] for _ in range(n)]
# color = ['R', 'B', 'G']
# answer1 = 0
# answer2 = 0
# for i in range(n):
#     for j in range(n):
#         if arr[i][j] in color and (visited[i][j][0] == 0 or visited[i][j][1] == 0):
#             visited[i][j][0] = arr[i][j]
#             tmp1, tmp2 = bfs(i, j, arr[i][j])
#             answer1 += tmp1
#             answer2 += tmp2
# for k in visited:
#     print(k)
# print(answer1, answer2)

# 얘는 그냥 통과
def bfs(i, j, color):
    q = []
    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        for di, dj in [[-1,0], [1,0], [0,-1], [0,1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0 and arr[ni][nj] == color:
                visited[ni][nj] = 1
                q.append((ni, nj))
    return 1
    
n = int(input())
arr = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
color = ['R', 'B', 'G']
answer1 = 0
answer2 = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] in color and visited[i][j] == 0:
            answer1 += bfs(i, j, arr[i][j])
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] in color and visited[i][j] == 0:
            answer2 += bfs(i, j, arr[i][j])
print(answer1, answer2)

