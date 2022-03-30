# 시간 초과
# import heapq
# import sys
# T = int(input())
# for _ in range(T):
#     n = int(input())
#     heap = []  # 최대 힙
#     min_heap = [] # 최소 힙
#     lst = [list(sys.stdin.readline().split()) for _ in range(n)]
#     for oper, num in lst:
#         if oper == 'I':
#             heapq.heappush(min_heap, int(num))
#             heapq.heappush(heap, (-int(num)))
#         elif num == '1':    # 최댓값 삭제
#             if heap:
#                 num = heapq.heappop(heap)
#                 min_heap.remove(-num)
#         elif num == '-1':
#             if heap:
#                 num = -heapq.heappop(min_heap)
#                 for i in range(len(heap)):
#                     if heap[i] == num:
#                         heap.remove(heap[i])
#                         break
#     print(-heap[0], min_heap[0]) if heap else print('EMPTY')


import heapq
import sys
T = int(input())
for _ in range(T):
    n = int(input())
    heap = []  # 최대 힙
    min_heap = [] # 최소 힙
    visited = [0] * n
    for i in range(n):
        oper, num = sys.stdin.readline().split()

        if oper == 'I':
            heapq.heappush(min_heap, (int(num), i))
            heapq.heappush(heap, (-int(num), i))
            visited[i] = 1
        else:
            if num == '1':    # 최댓값 삭제
                while heap and not visited[heap[0][1]]:
                    heapq.heappop(heap)
                if heap:
                    visited[heap[0][1]] = 0
                    heapq.heappop(heap)
            else:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)

                if min_heap:
                    visited[min_heap[0][1]] = 0
                    heapq.heappop(min_heap)

    if 1 not in visited:
        print('EMPTY')
    else:
        while heap and not visited[heap[0][1]]:
            heapq.heappop(heap)
        while min_heap and not visited[min_heap[0][1]]:
            heapq.heappop(min_heap)

        print(-heap[0][0], min_heap[0][0])

