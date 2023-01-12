string = input()
target = input()

idx, res = 0, 0
n = len(target)
while idx < len(string):
    if string[idx:idx+n] == target:
        res += 1
        idx += n
    else:
        idx += 1

print(res)