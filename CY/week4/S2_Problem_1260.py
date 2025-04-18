import sys
input = sys.stdin.readline 

from collections import deque
from collections import defaultdict
n, m, v = map(int, input().split()) 

graph = defaultdict(list) 

for _ in range(m):
    key, value = map(int, input().split()) 
    graph[key].append(value)
    graph[value].append(key)
    
visited = [False]*(n+1) 

# DFS 
# 그래프 자체를 받고, 방문 여부 리스트를 받고, 시작값을 받아서 이 함수 내 재귀호출 
def dfs(graph, visited, start):
    visited[start]=True # 시작 노드를 방문 처리 
    print(start, end=" ")
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    # 정점 번호가 작은 것을 먼저 방문하기 위해 정렬
    for value in sorted(graph[start]): # 이거 조건 없으면 sorted 없어도 되는듯 
        if not visited[value]:
            dfs(graph, visited, value)
    return visited # 방문 여부 리턴 
    
# BFS 
def bfs(graph, visited, start):
    # 방문 여부 리스트 초기화
    visited = [False] * (n+1)
    queue = deque([start]) # 큐 생성 및 시작 노드 추가
    visited[start] = True # 시작 노드 방문 처리
    
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        node = queue.popleft()
        print(node, end=" ") 
        
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for value in sorted(graph[node]):  # 번호가 작은 정점을 먼저 방문하기 위해 정렬
            if not visited[value]:
                queue.append(value)
                visited[value] = True
    
    return visited

dfs(graph, visited, v)
print()
bfs(graph, visited, v)