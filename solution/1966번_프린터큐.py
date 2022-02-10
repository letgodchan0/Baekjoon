n = int(input())

for _ in range(n):
    n, m = map(int, input().split())
    number = list(map(int, input().split()))
    index = 0
    printer = []
    for num in number:
        printer.append((num, index))
        index += 1
        
    tmp = printer.copy()
    cnt = 0
    # [1, 2, 3, 4], 2번 인덱스인 3이 언제 빠져 나가는지
    while True:
        check = printer.pop(0)
        if all(check[0] >= x[0] for x in printer):
            cnt += 1
        else:
            printer.append(check)
        if tmp[m] not in printer:
            print(cnt)
            break