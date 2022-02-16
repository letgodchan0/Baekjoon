t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    apt = [list(range(1, n+2))]
    for _ in range(k):
        tmp = [0] * n
        for i in range(len(tmp)):
            tmp[i] = sum(apt[0][:i+1])
        apt = [tmp] + apt
    print(apt[-k-1][n-1])