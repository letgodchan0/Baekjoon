def dfs(adjList, v, visited):
    visited[v] = True
    print(v, end=' ')  
    for i in adjList[v]:
        if not visited[i]:
            dfs(adjList, i, visited)
            
def bfs(adjList, v): 
    visit = [0] * (n + 1)
    q = []
    q.append(v)
    while q:
        tmp = q.pop(0)
        if not visit[tmp]:
            visit[tmp] = True
            print(tmp, end=' ')
            q.extend(adjList[tmp])
    return

n, m, v = map(int, input().split())
lst = []
for _ in range(m):
    lst.extend(list(map(int, input().split())))

adjList = [[] for _ in range(n+1)]
for i in range(m):
    n1, n2 = lst[i*2], lst[i*2+1]
    adjList[n1].append(n2)
    adjList[n2].append(n1)
adjList = list(map(sorted, adjList))
visited = [0] * (n + 1)
dfs(adjList, v, visited)
print()
bfs(adjList, v)