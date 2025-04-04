import sys 
# heap 사용 - 우선순위 큐니까 
import heapq
input = sys.stdin.readline

# N과 K 먼저 받기
n, k = map(int, input().split()) 

jewels = [] # 일단 정리

# 보석 정보
for x in range (n) : 
    weight, money = map(int, input().split())
    jewels.append([weight, money])
    
# 가방 리스트 
bags = []
for x in range (k) : 
    bags.append(int(input())) 
    
# 보석을 무게 기준으로 오름차순 정렬 - 현주야 고마워
jewels.sort()
# 가방도 오름차순 정렬
bags.sort()

total_money = 0
idx = 0 
temp = [] # 가방에 넣을 수 있는 가장 비싼 보석들의 최대 힙 (가격) 

# 작은 놈부터 간다! 
for bag in bags: 
    while idx < n and jewels[idx][0] <= bag: 
        # 현주야 고마워! 최대 힙을 위해 마이너스를 붙인다 
        heapq.heappush(temp, -jewels[idx][1])
        idx+=1
    if temp: 
        total_money-=heapq.heappop(temp)
         
print(total_money)