from collections import deque

n, k = map(int, input().split())
q = deque([])
q.append((n, 0))
visited = [0] * 100001
ans = 0
cnt = 100001
while q:
    number, time = q.popleft()
    if number == k:
        # 처음에 통과하는 time이 무조건 최소값
        if cnt > time:
            cnt = time
        # 최소 시간이랑 같을 때만 개수 체크
        if cnt == time:
            ans += 1
        continue

    for i in (2 * number, number - 1, number + 1):
        if 0 <= i < 100001 and not visited[i] and time < cnt:
            q.append((i, time+1))
        visited[number] =  1

print(cnt)
print(ans)