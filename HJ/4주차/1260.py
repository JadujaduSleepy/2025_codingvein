import sys
input = sys.stdin.readline
from queue import Queue

n, m, v = map(int, input().split())

edges = {(key+1):set() for key in range(n)}
visited = {(key+1):False for key in range(n)}
dfs_str = []
bfs_str = []

for _ in range(m):
    key, value = map(int, input().split())
    edges[key].add(value)
    edges[value].add(key)   # 양방향이므로


## DFS
def dfs(node):
    visited[node] = True
    dfs_str.append(str(node))
    for i in sorted(edges[node]):    # sort 안 하려고 set을 썼는데 여기서 그냥 정렬해줘야되나봅니다
        if not visited[i]:
            dfs(i)
dfs(v)


## BFS
visited = {(key+1):False for key in range(n)}   # 방문기록 초기화
q = Queue()

visited[v] = True
q.put(v)
while not q.empty():
    next = q.get()
    bfs_str.append(str(next))
    for node in sorted(edges[next]):
        if visited[node] == False:
            visited[node] = True
            q.put(node)

print(' '.join(dfs_str))
print(' '.join(bfs_str))