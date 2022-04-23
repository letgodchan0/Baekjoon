n = int(input())
m = int(input())
s = input()
# pn의 길이는 2n+1
cnt = 0
check = 0
i = 0
while i < m-2:
    if s[i] == 'I' and s[i+1] == 'O' and s[i+2] == 'I':
        check += 1
        i += 1
        if check == n:
            check -= 1
            cnt += 1
    else:
        check = 0
    i += 1

print(cnt)