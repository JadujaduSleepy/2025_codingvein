import sys

# 백준 제출시 삭제
sys.stdin = open('input.txt', 'r')

# 물품의 수 N과 준서가 버틸 수 있는 무게 K
N, K = map(int, input().split())

# 각 물건의 무게와 가치 저장
items = []
for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))



# dp 배열
dp = [[0 for i in range(K+1)] for i in range(N+1)]

for i in range(1, N+1): #물건..
    weight, value = items[i-1]
    for w in range(1, K+1): #무게..
        # 배낭보다 물건이 커서 못넣음
        if weight > w:
            dp[i][w] = dp[i-1][w]
        # 배낭에 물건 넣을 수 있음
        else:
            # 안넣는경우 vs 넣는경우
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value)
        
print(dp[N][K])