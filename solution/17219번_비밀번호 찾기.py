n, m = map(int, input().split())
answer = {}
for _ in range(n):
    tmp = input().split()
    answer[tmp[0]] = tmp[1]
for _ in range(m):
    print(answer[input()])