import sys
from collections import deque

# 백준 제출시 삭제
sys.stdin = open('input.txt', 'r')

N, M, V = map(int, input().split())

graph = {i: [] for i in range(1, N+1)}

for _ in range(M):
    a, b = map(int, input().split())
    if a not in graph :
        graph[a] = []
    if b not in graph :
        graph[b] = []
    graph[a].append(b)
    graph[b].append(a)

visited1 = [0] * (N+1) # 방문체크 배열 DFS
visited2 = [0] * (N+1) # 방문체크 배열 BFS

for key in graph:
    graph[key].sort()

def DFS(graph, visited, now):
    visited[now] = 1 # 방문처리
    print(now, end=' ')
    for neighbor in graph[now] :
        if not visited[neighbor] : #방문하지 않은 인접 노드
            DFS(graph, visited, neighbor)

DFS(graph, visited1, V)

print('\n', end='')

def BFS(graph, visited, now):
    queue = deque([now]) # 큐 초기화
    while queue: # 큐가 빌 때까지 반복함
        bottom = queue.popleft() # 큐에서 하나 뽑음
        if not visited[bottom] : # 방문 안한거면
            visited[bottom] = 1 # 방문처리
            print(bottom, end=' ') # 출력
            # 인접 노드들 중에 방문 안된거 삽입
            queue.extend([i for i in graph[bottom] if not visited[i]]) 

BFS(graph, visited2, V)