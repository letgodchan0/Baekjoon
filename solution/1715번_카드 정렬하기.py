import sys, heapq

n = int(input())
card, ans = [], 0
for _ in range(n):
    num = int(sys.stdin.readline())
    heapq.heappush(card, num)

while len(card) != 1:
    fir = heapq.heappop(card)
    sec = heapq.heappop(card)
    ans += fir + sec
    heapq.heappush(card, fir+sec)

print(ans)