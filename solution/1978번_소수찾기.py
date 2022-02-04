n = int(input())
numbers = list(map(int, input().split()))

def prime(number):
    if number == 1 or number == 0:
        return False
    for num in range(2, int(number**0.5)+1):
        if number % num:
            pass
        else:
            return False
    return True

cnt = 0
for number in numbers:
    if prime(number):
        cnt += 1
print(cnt)