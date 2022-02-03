m,  n = map(int, input().split())

def check(number):
    if number == 1:
        return False
    for num in range(2, int(number**0.5)+1):
        if number % num:
            pass
        else:
            return False
    return True

for num in range(m, n+1):
    if check(num):
        print(num)