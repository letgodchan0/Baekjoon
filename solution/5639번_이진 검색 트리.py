import sys
sys.setrecursionlimit(10**9)

def post_order(s, e):
    if s >= e:
        return
    root = pre_order[s]
    idx = s+1

    for i in range(s+1, e):
        if pre_order[i] > root:
            idx = i
            break

    post_order(s+1, idx)
    post_order(idx, e)
    print(root)
    return

pre_order = []
while 1:
    try:
        pre_order.append(int(sys.stdin.readline()))
    except:
        break

post_order(0, len(pre_order))