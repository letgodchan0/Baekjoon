while True:
    stack = [0]
    check = True
    string = input()
    if string == '.':
        break
    for s in string:
        if s == '(' or s=='[':
            stack.append(s)
        elif s == ')':
            if stack[-1] == '(':
                stack.pop(-1)
            else:
                check = False
        elif s ==']':
            if stack[-1] == '[':
                stack.pop(-1)
            else:
                check = False

    print('yes') if check and stack[-1] == 0 else print('no')