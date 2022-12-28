def dfs(t):
    global check

    if s == t:check = True
    if len(t) == 0:
        return

    if t[-1] == 'A':
        dfs(t[:-1])
    if t[0] == 'B':
        dfs(t[1:][::-1])

s = input(); t = input()
check = False

dfs(t)
print(1 if check else 0)