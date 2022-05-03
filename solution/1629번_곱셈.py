a, b, c = map(int, input().split())

def dac(a, n):
    if n == 1:
        return a % c
    else:
        tmp = dac(a, n // 2)
        if n % 2 == 0:
            return (tmp * tmp) % c
        else:
            return (tmp * tmp * a) % c

print(dac(a, b))

print(pow(a, b, c))