n = int(input())
for _ in range(n):
    height, width, nth = map(int, input().split())
    if height > nth:
        print(str(nth)+'01')
    else:
        if nth % height:
            a = str(nth%height)
            if  nth // height < 9:
                b = '0' + str(nth // height + 1)
            else:
                b = str(nth//height + 1)
        else:
            a = str(height)
            if  nth // height < 10:
                b = '0' + str(nth // height)
            else:
                b = str(nth // height)
        print(a+b)