# 가로등 M개, 가로등 위치 x
# 가로등의 높이만큼 주위를 비출 수 있음
# 최소한의 높이로 굴다리 모든 길 0-N을 밝히고자 함.
# 가로등은 모두 높이가 같아야 하고, 정수이다.

# 첫줄 굴다리 길이 N
# 가로등 개수 M
# 설치할 수 있는 가로등의 위치 x -> 오름차순

 
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
xx = list(map(int, input().split()))    # x는 중복되지 않으며 정수. 오름차순으로 입력받음. x는 정렬된 상태.


## h의 범위 중 가운데가 true면 앞에서 search, false면 뒤에서 search

# 불켜기
def light(h):
    road = [0]*n
    for x in xx:
        for i in range(max(0, x-h), min(n, x+h) ):
            road[i] = 1 
    # 모두 불이 켜졌는가?
    print(road)
    return sum(road) == n

left = 0
right = n
while left < right:
    mid = (left + right) // 2 + 1
    print("현재 mid:", mid, "left: ", left, "right:", right )
    if mid == left or mid == right:
        break
    if light(mid):    # 모두 불이 켜져 있음 => h는 더 짧아도 됨
        print("불이 모두 켜져 있습니다")
        right = mid
    else:  # 안 켜진 구간이 있음 => h는 더 길어야 함
        print("불이 안 켜진 곳이 있습니다")
        left = mid

print(mid)







## 이거 왜 틀린지 모르겠음
# 가로등 범위: (x - h, x + h)

# for h in range(1, n+1):
#     # print("h: ", h)
#     road = [0]*n
#     for x in xx:
#         # print("x: ", x)
#         lwr, upr = max(0, x-h), min(n, x+h)
#         # print("lwr: ", lwr)
#         # print("upr: ", upr)
#         road[lwr:upr] = [1]*(upr - lwr)    # 불 켜진 자리는 1
#         # print("길: ", road)
#     if sum(road) == n:
#         ans = h
#         break

# print(ans)