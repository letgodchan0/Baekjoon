def empty():
    print(0) if queue else print(1)
def size():
    print(len(queue))
def push(item):
    queue.append(item)    
def pop():
    print(queue.pop(0)) if queue else print(-1)
def front():
     print(queue[0]) if queue else print(-1)
def back():
     print(queue[-1]) if queue else print(-1)

import sys
n = int(input())
queue = []
for _ in range(n):
    order = sys.stdin.readline().strip('\n').split()
    if order[0] == 'push':
        push(order[1])
    elif order[0] == 'pop':
        pop()
    elif order[0] == 'front':
        front()
    elif order[0] == 'back':
        back()
    elif order[0] == 'size':
        size()
    else:
        empty()