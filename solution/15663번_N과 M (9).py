from itertools import permutations

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = []
result = set(result)
for case in permutations(arr, m):
    if case not in result:
        result.add(case)
        print(' '.join(map(str, case)))