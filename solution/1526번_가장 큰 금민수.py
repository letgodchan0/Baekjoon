number = int(input())

res = []

for num in range(1, number+1):
    check = str(num).replace('4', '')
    check = check.replace('7', '')

    if not check:
        res.append(num)
    
print(max(res))