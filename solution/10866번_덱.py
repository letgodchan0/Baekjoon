def empty():
    print(0) if deque else print(1)
def size():
    print(len(deque))
def push_front(item):
    global deque
    deque = [item] + deque
def push_back(item):
    deque.append(item)
def pop_front():
    print(deque.pop(0)) if deque else print(-1)
def pop_back():
    print(deque.pop(-1)) if deque else print(-1)
def front():
     print(deque[0]) if deque else print(-1)
def back():
     print(deque[-1]) if deque else print(-1)

import sys
n = int(input())
deque = []
for _ in range(n):
    order = sys.stdin.readline().strip('\n').split()
    if order[0] == 'push_front':
        push_front(order[1])
    elif order[0] == 'push_back':
        push_back(order[1])
    elif order[0] == 'pop_front':
        pop_front()
    elif order[0] == 'pop_back':
        pop_back()
    elif order[0] == 'front':
        front()
    elif order[0] == 'back':
        back()
    elif order[0] == 'size':
        size()
    else:
        empty()