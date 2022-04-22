from collections import deque
import sys

def f(lst):
    s = '['
    s += ','.join(map(str, lst))
    s +=']'
    return s

t = int(input())
for _ in range(t):
    p = input()
    n = int(input())
    string = sys.stdin.readline().replace('[', '').replace(']','').rstrip('\n')
    if string:
        string = string.split(',')
    else:
        string = []

    lst = deque(string)

    rev = 1
    check = True
    for s in p:
        if s == 'R':
            rev = 1 - rev
        elif s == 'D':
            if lst:
                if rev:
                    lst.popleft()
                else:
                    lst.pop()
            else:
                check = False
                break
    if not rev:
        lst.reverse()

    print(f(list(lst)) if check else 'error')
