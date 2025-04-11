import sys 
input = sys.stdin.readline

n = int(input()) # 길이 N 
m = int(input()) # 갯수 M
lamps = list(map(int, input().split())) # 받자마자 int로 매핑해서 list로 전환 

# 높이는 모두 같아야 한다 (height 동일) 
# 가로등 위치 x : 오름차순 

def cover(lamps, height):
    # lamps 내 cover 여부 확인 
    for x in range(len(lamps)-1):
		    # 두 램프 사이가 2xheight보다 크면 커버 못하니까 False 
        if (lamps[x+1]-lamps[x])>2*height:
           return False
    return True # False 

# 시작점 : 첫 가로등 위치. 0까지 커버해야하니까 / N = 끝 가로등 위치 (끝까지 커버해야하니까) 
# 위 둘 중 큰 값을 시작 height로 잡기 
# 끝점 : N (굴다리 길이) 
start = max(lamps[0], n-lamps[-1]) # 상한 하한 다 정해놨으니까 이쪽은 기본적으로 커버
end = n
height = 0 # 최소값을 구하는 거기도 하고 0부터 하면 그냥 커버못한 채 시작해서 mid만 이동함
# height를 저장 못한다는 뜻 .. 

while start<=end:
    mid = (start + end) // 2 
    if not cover(lamps, mid):
        start = mid+1 # 오른쪽 확인 
    else:
        # 최소로 낮아질 수 있는지도 검토해줘야됨 
        # 커버가 됐으면 줄어도 되는지 확인해주기 
        height = mid
        end = mid -1 
    
        
print(height) 