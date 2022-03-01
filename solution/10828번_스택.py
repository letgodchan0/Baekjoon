def empty():
    print(0) if stack else print(1)

def size():
    print(len(stack))
def top():
    print(stack[-1]) if stack else print(-1)
def push(item):
    stack.append(item)
    
def pop():
    print(stack.pop(-1)) if stack else print(-1)

import sys
n = int(input())
stack = []
for _ in range(n):
    order = sys.stdin.readline().strip('\n').split()
    if order[0] == 'push':
        push(order[1])
    elif order[0] == 'pop':
        pop()
    elif order[0] == 'top':
        top()
    elif order[0] == 'size':
        size()
    else:
        empty()
 