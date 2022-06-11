import sys
n = int(input())
number = list(sys.stdin.readline().split())
stack = [number[0]]

# 일단 스택에 다 넣자, 스택을 항상 갱신하자!
for i in range(1, n):
    tmp = stack.pop()
    # 스택에서 빼낸 값보다 현재 값이 더 우선순위가 있다면
    if int(tmp + number[i]) <= int(number[i] + tmp):
        stack.append(tmp)
        stack.append(number[i])
    # 스택 갱신, 스택에서 빼낸 값이 더 우선순위가 있음
    else:
        # 스택에 값이 있다면 갱신해주고
        check = []
        if stack:
            while stack:
                last_value = stack.pop()
                if int(last_value + number[i]) < int(number[i] + last_value):
                    stack.append(last_value)
                    break
                else:
                    check.append(last_value)
            stack.append(number[i])
            if check:
                check.reverse()
                stack.extend(check)
            stack.append(tmp)
        # 스택이 비어 있다면
        else:
            stack.append(number[i])
            stack.append(tmp)
stack.reverse()
answer = ''.join(stack)
print(0) if answer[0] == '0' else print(answer)
