import sys

t = int(input())

for _ in range(t):
    n = int(input())
    phones = [sys.stdin.readline().rstrip() for _ in range(n)]
    phones.sort()

    check = True
    for i in range(len(phones)-1):
        if phones[i][:min(len(phones[i]), len(phones[i+1]))] == phones[i+1][:min(len(phones[i]), len(phones[i+1]))]:
            check = False
            break

    print("YES" if check else "NO")