t = int(input())
for _ in range(t):
    n, word = input().split()
    answer = ''
    for s in word:
        answer += s*int(n)
    print(answer)