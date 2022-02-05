from math import gcd
m, n = map(int, input().split())

print(gcd(m,n))
print((m*n)//gcd(m,n))


# 최대공약수
def gcd(m, n): 
    if n == 0:
        return m
    return gcd(n,m%n)
m, n = map(int, input().split())
print(gcd(m, n))
# 최소공배수
print(int(m*n/gcd(m,n)))