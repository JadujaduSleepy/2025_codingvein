# 히오스 36264KB 2460ms
import sys

# 백준 제출시 삭제
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())

character_levels = []
for _ in range(N):
    level = int(input())
    character_levels.append(level)

character_levels.sort() #오름차순 정렬

T = character_levels[0] #초기 T

for i in range(N-1) :
    gap = character_levels[i+1] - character_levels[i]
    if gap == 0:
        continue
    if (K>=(gap*(i+1))) : # 레벨 균등 분배 가능
        K = K-gap*(i+1)
        T = T+gap
    else : # 균등 분배 불가능
        T += K//(i+1)
        K=0
        break

# 분배까지 완료된 이후 남은 K 처리
if (K>0) :
    T += K//N

print(T)
