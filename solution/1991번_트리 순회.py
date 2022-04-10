# 전위 순회
def pre_order(v):
    if v:   # 0번 정점이 없으므로... 0번은 자식이 없는 경우를 표시
        print(v, end = '')   # visit(v), vis
        pre_order(ch1[check[v]])   # 왼쪽 자식으로 이동
        pre_order(ch2[check[v]])   # 오른쪽 자식으로 이동

# 중위 순회
def in_order(v):
    if v:
        in_order(ch1[check[v]])
        print(v, end = '')
        in_order(ch2[check[v]])

# 후위 순회
def post_order(v):
    if v:
        post_order(ch1[check[v]])
        post_order(ch2[check[v]])
        print(v, end = '')

import sys
n = int(input())
ch1 = [''] * (n+1)
ch2 = [''] * (n+1)
check = {}
for i in range(1, n+1):
    x, y, z = sys.stdin.readline().split()
    check[x] = i
    if y != '.':
        ch1[i] = y
    if z != '.':
        ch2[i] = z

pre_order('A')
print()
in_order('A')
print()
post_order('A')
