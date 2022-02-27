import math
n, k = map(int, input().split())
print(math.factorial(n)//math.factorial(k)//math.factorial(n-k))

# 직접 만들기
def f(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans
def find(n, r):
    return f(n) // f(r) // f(n-r)