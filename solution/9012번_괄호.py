T = int(input())
for _ in range(T):
    string = input()
    stack = []
    check = True
    for s in string:
        if s == '(':
            stack.append(s)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                check = False
    print('YES') if check and not stack else print('NO')