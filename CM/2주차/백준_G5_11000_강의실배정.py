import heapq
import sys

N = int(input())
C = []
h = []
for i in range(N):
    C.append(list(map(int, sys.stdin.readline().split())))

# 시작 시간 기준으로 정렬
C = sorted(C,key = lambda x: x[0])

for i in range(N):
    # 젤 빨리 끝나는게 현재 일정 시작시간보다 빠르게 끝남
    if len(h) != 0 and h[0]<= C[i][0]:
        heapq.heappop(h) # 제거(재사용됨)
    heapq.heappush(h,C[i][1]) # 지금거 종료시간 힙에 넣음
    
print(len(h))