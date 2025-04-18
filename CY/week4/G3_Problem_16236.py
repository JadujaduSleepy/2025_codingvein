import sys
input = sys.stdin.readline

from collections import deque # BFS 쓸 것임
n = int(input().rstrip()) # nxn
space = [] # 저장 공간 
for _ in range(n):
    space.append(list(map(int, input().split())))

# 사이즈 체크 함수가 있어야될지도? 
def size_check(eating, size):
    eating += 1 
    if eating == size:
        size +=1 
        eating = 0 
    return eating, size

e_time = 0 # return할 time. 이건 반복할 때마다 +1 해줘야겠는데? 
size = 2 # 아기상어 사이즈 
eating = 0 
# 현재 상어 위치 
for i in range(n):
    for j in range(n):
        if space[i][j]==9:
            y = i
            x = j

def bfs(y, x): # 안 받고 그냥 아니다 받아야되겠다 바뀌니까 
    global size
    global space

    que = deque() 
    # direction 
    dx = (0, 0, -1, 1)
    dy = (-1, +1, 0, 0)

    visited = [[-1] * n for _ in range(n)] 
    
    # space[y][x] - 아기 상어 첫 위치 
    visited[y][x] = 0 
    que.append((y, x)) 

    fish = [] # visited가 거리나마찬가지니까 거리 / ny / nx 
        
    while que:
        y, x = que.popleft()
        for i in range (4): 
            ny = y + dy[i]
            nx = x + dx[i] 
            
            # 여기서부터 조건문 
            # 1. Grid를 벗어난다 - continue 
            if not (0<=y<n and 0<=x<n) :
                continue
            
            # 2. 현재 사이즈보다 큰 경우 
            if space[ny][nx] > size:
                continue 
            
            # 2-1. 
            # 방문 여부 체크 
            if visited[ny][nx] != -1 :
                continue # 패스패스 
            
            if 0 < space[ny][nx] <= size: 
                # 같은 경우 이동만 하고
                visited[ny][nx] = visited[y][x]+1
                que.append((ny, nx)) # 갈 수 있는 곳이라면 append 
                
                if 0<space[ny][nx]<size:
                    fish.append((visited[ny][nx], ny, nx)) 
    if fish:
        # visited 거리 - ny (왼쪽부터) - nx
        fish.sort() 
        return fish[0] # 처무기까지 걸리는 거리, 좌 표 
    else:
        return (-1, -1, -1)

while True:
    menow = bfs(y, x)
    
    if menow == (-1, -1, -1):
        break

    else:
        distance, ny, nx = menow
        e_time += distance # total_time에 그 거리를 더해주고 

        space[ny][nx] = 0 # 내가먹엇어 -> 0 

        y = ny
        x = nx

        eating, size = size_check(eating,size)

print(e_time)
