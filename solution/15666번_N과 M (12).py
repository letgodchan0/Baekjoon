from itertools import combinations_with_replacement

n, m = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()
lst = list(combinations_with_replacement(lst, m))
res = sorted(list(set(lst)))

for r in res:
    print(*r)