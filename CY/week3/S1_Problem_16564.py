import sys
input = sys.stdin.readline

levels = []
num, total_level = map(int, input().split()) 
for i in range(num):
    levels.append(int(input()))

levels.sort() # 정렬

# start / end / mid 
min_max = 0

# 올려야 하는 캐릭터의 수가 2개 이상인 경우 
if num>1:
    # 만약 가장 낮은 레벨과 그 다음 레벨의 차가 총 올릴 수 있는 레벨보다 큰 경우 
    if (levels[1]-levels[0])-total_level>0:
        levels[0] = levels[0] + total_level
        min_max = levels[0] 
    
    else: # 그외 - 여기서부터 시작
        # 가장 낮은 것과 그다음 낮은 두 개를 맞춰주고 시작해봤음 (별 의미X)
        now_up = levels[1]-levels[0]
        total_level -= now_up
        levels[0] += now_up
        
        # min 레벨을 최대화하기 위함
        # 여기서 Key값은 min 레벨이라고 볼 수 있다... 
        # 따라서 min 레벨의 가능 범위를 start / end로 지정해둠 
        start = levels[0]
        end = levels[-1]+total_level 
        
        while start <= end:
            need = 0
            mid = (start+end)//2 
            
            # min 레벨이 되기 위해 필요한 레벨 합을 need라고 한다 
            for i in range(num):
                need += max(0, mid-levels[i])

            # 이때 need가 업할 수 있는 레벨보다 높은 경우 min을 낮추는 범위에서 서치     
            if need > total_level:
                end = mid-1

            # 그외: 더 높일 수 있는지 검토토    
            else:
                min_max=mid
                start = mid+1
else:
    # 올릴 수 있는 캐릭터가 1개인 경우
    min_max=levels[0]+total_level

print(min_max)