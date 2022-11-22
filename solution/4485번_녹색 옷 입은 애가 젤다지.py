import sys, heapq

def dijkstra():
    heap = []
    cost[0][0] = arr[0][0]
    heapq.heappush(heap, (arr[0][0], 0, 0))
    while heap:
        weight, x, y = heapq.heappop(heap)
        if x == n-1 and y == n-1:
            return cost[x][y]

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                tmp = weight + arr[nx][ny]
                if cost[nx][ny] > tmp:
                    cost[nx][ny] = tmp
                    heapq.heappush(heap, (tmp, nx, ny))
cnt = 1
while True:
    n = int(input())
    if n == 0:break
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    cost = [[sys.maxsize] * n for _ in range(n)]
    print(f'Problem {cnt}: {dijkstra()}')
    cnt += 1