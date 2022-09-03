def dfs(x, y):
    stack = [(x,y,0, arr[x][y])]
    lst = []
    while stack:
        x, y, cnt, six = stack.pop()
        if cnt == 5 and six not in lst:
            lst.append(six)

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 5 and 0 <= ny < 5 and cnt < 5:
                stack.append((nx, ny, cnt + 1, six+arr[nx][ny]))
    return lst

arr = [list(input().split()) for _ in range(5)]
answer = []
for i in range(5):
    for j in range(5):
        result = dfs(i,j)
        for res in result:
            if res not in answer:
                answer.append(res)

print(len(answer))
