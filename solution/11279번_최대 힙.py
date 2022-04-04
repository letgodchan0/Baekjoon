import heapq
import sys
n = int(input())
heap = [0] * n
for _ in range(n):
    num = int(sys.stdin.readline())
    if num:
        heapq.heappush(heap, -num)
    else:
        print(-heapq.heappop(heap))
