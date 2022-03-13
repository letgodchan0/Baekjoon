import sys
n, m = map(int, input().split())
lst = [sys.stdin.readline() for _ in range(n+m)]
answer = {k:0 for k in lst}

for k in lst:
    answer[k] = answer.get(k, 0) + 1
result = []
for k in answer.keys():
    if answer[k] == 2:
        result.append(k)
print(len(result))
for s in sorted(result):
    print(s.rstrip('\n'))