from sys import stdin as s
import heapq

n, k = map(int, s.readline().split())

# 보석
## 무게, 가격 순서
jewels = [list(map(int, s.readline().split())) for i in range(n)]
jewels.sort(key=lambda x: (x[0], x[1]))

# 상덕이 가방
bags = [int(s.readline()) for i in range(k)]
bags.sort()

# 훔친가격총합
S = 0
# 같은무게들 임시저장
temp = []
for bag in bags:
    # 보석이 가방의 무게를 넘지 않을 때까지 꺼내서 담기
    while jewels and jewels[0][0] <= bag:
        # 가방에 들어가는 보석들 임시저장 (가격만, 비싼 순으로)
        heapq.heappush(temp, -jewels[0][1])
        heapq.heappop(jewels)
    ######## 저장끝 ##########
    if temp:
        S -= temp[0]   # 가장비싼거 더하기
        heapq.heappop(temp)
print(S)
