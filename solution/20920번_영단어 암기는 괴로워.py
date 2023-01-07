import sys
n, m = map(int, input().split())
words = {}
for _ in range(n):
    string = sys.stdin.readline().rstrip()
    if len(string) >= m:
        words[string] = words.get(string, 0) + 1

lst = list(words.keys())
lst.sort(key = lambda x : (-words[x], -len(x), x))

for l in lst:
    print(l)