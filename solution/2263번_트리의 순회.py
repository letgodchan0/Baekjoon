import sys
sys.setrecursionlimit(10 ** 6)

def check(left, right, left_post, right_post):

    if left > right or left_post > right_post:
        return
    parent = post_order[right_post]
    print(parent, end = " ")

    S_idx = idx[parent]
    new_left = S_idx - left

    check(left, S_idx - 1, left_post, (left_post + new_left) - 1)
    check(S_idx + 1, right, left_post + new_left, right_post - 1)

n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

idx = [0] * (n+1)
for i in range(n):
    idx[in_order[i]] = i

check(0, n-1, 0, n-1)