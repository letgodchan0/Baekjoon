def dfs(num):
    if num == m:
        print(*lst)
        return
    for i in range(n):
        if check[i]:
            continue
        lst.append(i+1)
        dfs(num+1)
        lst.pop()
        check[i] = 1
        for j in range(i+1, n):
            check[j] = 0

n, m = map(int, input().split())
check = [0] * n
lst = []
dfs(0)