s = input()
lst = set()
for i in range(1, len(s)+1):
    for j in range(len(s)-i+1):
        lst.add(s[j:i+j])
print(len(lst))