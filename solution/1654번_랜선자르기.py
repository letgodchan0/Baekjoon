K, N = map(int, input().split())

lengths = []
for _ in range(K):
    lengths.append(int(input()))

tmp = sum(lengths) // N
while True:
    total = sum([length // tmp for length in lengths])
    if total >= N:
        print(tmp)
        break
    tmp -= 1