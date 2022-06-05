def check(n, s):
    return s*power(n, num-2) % num

def power(base, exponent):
    if exponent == 1:
        return base % num
    if exponent % 2 == 0:
        newbase = power(base, exponent // 2)
        return (newbase * newbase) % num
    else:
        return base * power(base, exponent-1) % num

answer = 0
m = int(input())
num = 1000000007
for _ in range(m):
    n, s = map(int, input().split())
    answer += check(n, s)
    answer %= num
print(answer)