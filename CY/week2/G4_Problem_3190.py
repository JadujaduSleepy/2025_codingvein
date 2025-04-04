import sys 
input = sys.stdin.readline
from collections import deque
size = int(input()) 
limit = size+1 # 좌표 설정할 때 벽 제한 설정 
apple_num = int(input()) 
total_time = 0
apple = [] # 일단 list로 

def move (time, direction, snake, apple, limit):
    """
        args : time - 이동 time. 함수에서는 1초에 한 칸씩 움직이는 걸 time만큼 반복한다 
        direction : 이동 디렉션. 시작 방향이 우측이기 때문에 [우, 하, 좌, 상] = 1, 2, 3, 4으로 지정. 
        snake : 뱀 자료구조 (여기서는 덱)
        apple : 사과 좌표 리스트
        limit : 보드 사이즈 리밋. 

        해당 함수에서는 오로지 이동만 하며 direction 변경은 진행하지 않음. 
        이동한 시간만큼만 timer로 return한다. 
    """
    x = [1, 0, -1, 0] # direction이 1~4일 때 -1 인덱스값 
    # y = [0, -1, 0, 1] # direction이 1~4일 때 -1 인덱스값
    # 아헐설마?
    y = [0, 1, 0, -1] 
    timer = 0

    while timer<time:
        # 1초 뒤
        timer += 1 
        head = snake[-1] # (x, y) 형식으로 저장됨 
        head_x, head_y = head[0], head[1] 

        # 새로운 머리값 : direction은 1부터 시작이라 -1 하여 사용해야함 
        # brand_new_head = [ head_x + x[direction-1], head_y + y[direction-1] ]
        brand_new_head = (head_x + x[direction-1], head_y + y[direction-1])
        
        # 벽 충돌 금지 
        # 0보다 작거나 같아지면 안되고, limit보다 크거나 같아지면 안된다 
        if brand_new_head[0]>=limit or brand_new_head[1]>=limit or brand_new_head[0]<=0 or brand_new_head[1]<=0:
            # 초과하는 경우 바로 진행 시간을 return 
            return timer
            
        # 스스로의 몸과 부딪히면 안된다 
        if brand_new_head in snake:
            # 기록 좌표 속 나의 머리가 있다면 안됨 
            return timer
            
        # 그렇지 않은 경우 머리를 append한다 
        snake.append(brand_new_head)
        
        # 꼬리 관련 작업을 위해 사과 식사 여부를 체크한다
        콱 = 0 
        for i in range (len(apple)):
            # 머리의 좌표가 사과의 좌표와 같다면 사과를 해당 리스트에서 pop하고 break한다 
            if brand_new_head == apple[i]: 
                apple.pop(i)
                콱=1 # 먹었음을 표기
                break 

        # 먹지 않았다면 꼬리를 제거한다
        if 콱==0:
            snake.popleft()
    return timer

# 사과 위치 
for i in range (apple_num) : 
    x, y = map(int, input().split()) 
    # [[x1, y1], [x2, y2] ...]
    apple.append([x, y])
    
# 방향 가이드
direction = 1 # [우, 하, 좌, 상] = 1, 2, 3, 4
x = [1, 0, -1, 0] # direction이 1~4일 때 -1 인덱스값 
y = [0, 1, 0, -1] # direction이 1~4일 때 -1 인덱스 값

direct_num = int(input())
snake = deque([(1, 1)]) 

save = []
for i in range(direct_num) : 
    time, command = input().split()
    time=int(time)
    save.append((time, command))

for time, command in save:
    input_time = time - total_time
    # 함수 호출하여 timer - 진행 시간을 받은 후 total time에 더해준다 
    moving_time = move(input_time, direction, snake, apple, limit)
    total_time += moving_time
    # 근데 충돌했을 경우에 떠나야됨 
    if moving_time < input_time:
        break
    
    # 방향 전환 
    if command == 'L':
        direction = (direction+3)%4 
        # 4로 나누면 0이 되는 경우는 direction 인덱스를 4로 바꿔준다
        if direction == 0:
            direction = 4
    else:
        direction = (direction+1)%4
        # 마찬가지
        if direction == 0:
            direction = 4
            
print(total_time)