import heapq
import sys
heap = []
n = int(input())
for _ in range(n):
    num = int(sys.stdin.readline())
    if num:
        heapq.heappush(heap, num)
    else:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
