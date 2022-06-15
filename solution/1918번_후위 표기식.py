string = input()
N = len(string)
isp = {'+': 1, '-' : 1, '*': 2, '/': 2, '(' : 0} # 스택 push 전 우선순위
icp = {'+': 1, '-' : 1, '*': 2, '/': 2, '(' : 3} # 스택 내부 우선순위
stack = [0] * N # 연산자를 담는 곳
top = -1
postfix = '' # 최종 후위표기식
for i in range(N):
    if 'A' <= string[i] <= 'Z': # 피연산자면 postfix에 붙여주기
        postfix += string[i]
    # 연산자라면, 스택 내부
    elif string[i] == '+' or string[i] == '*' or string[i] == '-' or string[i] =='/':
        # 토큰이 스택의 top 우선순위보다 높을 때까지 스택에서 pop해서 postfix에 붙여준다.
        while top > -1 and icp[string[i]] <= isp[stack[top]]:

            postfix += stack[top]
            stack[top] = 0
            top -= 1
        # 스택이 비어 있거나 토큰이 스택의 top보다 우선순위가 높다면 그대로 스택에 push
        top += 1
        stack[top] = string[i]
    elif string[i] == '(':
        top += 1
        stack[top] = string[i]
    else:
        # 왼쪽 괄호 나올 때까지 stack을 pop해서 postfix에 푸쉬하기
        while stack[top] != '(':
            postfix += stack[top]
            stack[top] = 0
            top -= 1
        # 왼쪽 괄호 만나면 pop 하기
        if stack[top] == '(':
            stack[top] = 0
            top -= 1
# 스택에 남아있는 연산자 모두 pop하여 postfix에 푸쉬하기
while top > -1:
    postfix += stack[top]
    top -= 1
print(postfix)