import sys
def find(x):
    while x != parent[x]:
        x = parent[x]
    return x

def union(x, y):
    parent[find(y)] = find(x)

V = int(input())
E = int(input())
# 1번노드와 2번 노드가 연결되면 5의 가중치가 필요하다
arr = []
for _ in range(E):
    node1, node2, w = map(int, sys.stdin.readline().split())
    arr.append((w, node1, node2))
# 오름차순 정렬을 해서 가중치가 최소인걸 가장 먼저 선택을 해야되니까
arr.sort()
# 신장트리가 완성되려면 노드의 개수 - 1개 만큼의 간선이 존재이 존재하면 된다
parent = [i for i in range(V+1)]
n = V - 1
cnt = 0
total = 0
for w, node1, node2 in arr:
    # 사이클이 존재하면 신장트리가 될 수 없어요.
    if find(node1) != find(node2):
        cnt += 1
        union(node1, node2)
        total += w
        if cnt == n:
            break
print(total)
