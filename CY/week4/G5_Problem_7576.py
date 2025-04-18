import sys
input = sys.stdin.readline

from collections import deque

m, n = map(int, input().split())
box = []

for _ in range(n):
    box.append(list(map(int, input().split())))

# BFS 함수 구현 
def bfs(box):
    que = deque() # 익은 토마토만이 들어갈 수 있는 큐 
    # 방향을 정의한다 
    dy = (-1, +1, 0, 0)
    dx = (0, 0, -1, +1)
    
    # 익은 틈메이러를 전부 넣는다 
    for i in range (n):
        for j in range(m): 
            if box[i][j]==1:
                que.append((i, j))
    # 이제 진짜 BFS
    while que:
        y, x = que.popleft() # 현재 좌표를 뱉어준다
        
        # 그 주변 틈메이러를 확인한다 
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            # 그리드를 탈출하면 pass 
            if not (0<=nx<m and 0<=ny<n): 
                continue
            
            # 아니면 따악 익어준다 (건너온 좌표 +1로 바까준다) 
            if box[ny][nx]==0:
                box[ny][nx] = box[y][x] + 1 # 이게 곧 시간 좌표가된다
                que.append((ny, nx)) # 익었으니 좌표를 큐에 꾸겨넣어줌

    dtime = 0 
    # 박스를 다 돌아서 가장 높은 숫자를 dtime으로 바꾸고 
    # 0이 존재하면 -1를 뱉는다. 단!! 만약 위의 max값이 1이라면 그건 첨부터 익은 박스
    for i in range(n):
        for j in range(m):
            if box[i][j] == 0 : 
                return -1
            else:
                if box[i][j] > dtime:
                    dtime = box[i][j]           
    if dtime == 1:
        return 0
    else:    
        # 처음부터 1일이 아니라서 1을 빼줘야 했다 
        return dtime-1

print(bfs(box))