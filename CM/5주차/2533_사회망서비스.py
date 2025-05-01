import sys
sys.setrecursionlimit(1000001)

# 백준 제출시 삭제
sys.stdin = open('input.txt', 'r')

# 정점의 수 N 입력 받기
N = int(sys.stdin.readline())

# 그래프 초기화 (인접 리스트)
graph = [[] for _ in range(N + 1)]

# N-1개의 에지 정보 입력 받기
for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    # 양방향 그래프로 저장
    graph[u].append(v)
    graph[v].append(u)

dp = [[-1, -1] for _ in range(N + 1)]
# 작은문제로 분할하면?
# 결국 개개인이 얼리어답터인지vs아닌지 2중 택1 문제
# DFS로 탐색?
# dp 구성
# dp[노드번호][얼리어답터여부?] = 최소 얼리어답터 수 저장
# 위에서부터 내려가는 서브트리로 생각하는건가
visited = [0] * (N + 1)
# dfs
def DFS(visited, now, graph):
    visited[now] = 1

    dp[now][1] = 1 # 노드가 얼리어답터임
    dp[now][0] = 0 # 노드가 얼리어답터 아님
    
    for child in graph[now]: #자식 순회하면서 dp에 더해줌
        if not visited[child]:
            DFS(visited, child, graph) # 자식 DFS로 순회해서 계산
            # 현재노드가 얼리어답터면 자식들은 얼리어답터 아니어도 상관없음
            dp[now][1] += min(dp[child][0], dp[child][1])
            # 현재노드가 얼리어답터 아니면 자식들은 무조건 얼리어답터여야됨
            dp[now][0] += dp[child][1]

DFS(visited, 1, graph)

print(min(dp[1][0], dp[1][1]))