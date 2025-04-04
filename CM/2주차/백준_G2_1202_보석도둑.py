# 2025-04-02
# https://www.acmicpc.net/problem/1202

import sys
import heapq

# 백준 제출시 삭제
sys.stdin = open('input.txt', 'r')

N, K = map(int, sys.stdin.readline().split())

jewels = []
for _ in range(N):
    M, V = map(int, sys.stdin.readline().split())
    heapq.heappush(jewels, (M,V))

bags = []
for _ in range(K):
    C = int(sys.stdin.readline())
    bags.append(C)

bags.sort()
temp = []
answer = 0;

for bag in bags :
    # 가방에 들어가는 모든 보석을 찾음
    while jewels and jewels[0][0] <= bag :
            select = heapq.heappop(jewels) # 후보군
            heapq.heappush(temp, (-select[1], select[0])) # 이거는 가치 높은순

    if temp : # 뽑아놓은 보석이 존재함
        bestValue = heapq.heappop(temp)
        answer += -bestValue[0]

    # 없으면 그 가방엔 넣을수 있는게 없는것임

print(answer)
            