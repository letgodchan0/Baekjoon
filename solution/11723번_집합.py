def add(x):
    global s
    if x not in s:
        s.append(x)
def remove(x):
    global s
    if x in s:
        s.remove(x)
def check(x):
    global s
    if x in s:
        return 1
    else:
        return 0
def toggle(x):
    global s
    if x in s:
        s.remove(x)
    else:
        s.append(x)
def all():
    global s
    s = list(range(1, 21))
def empty():
    global s
    s = []

import sys
s = []
n = int(input())
for _ in range(n):
    tmp = sys.stdin.readline().split()
    if len(tmp) > 1:
        res, num = tmp[0], tmp[1]
    else:
        res = tmp[0]
    if res == 'add':
        add(int(num))
    elif res == 'remove':
        remove(int(num))
    elif res == 'check':
        print(check(int(num)))
    elif res == 'toggle':
        toggle(int(num))
    elif res == 'all':
        all()
    else:
        empty()