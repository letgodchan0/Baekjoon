word = input().upper()
check = {}
for char in word:
    check[char] = check.get(char, 0) + 1
max_char = max(check.values())
cnt = 0
word = ''
for char in check.keys():
    if check.get(char) == max_char:
        cnt += 1
        word = char
if cnt > 1:
    print('?')
else:
    print(word)