import sys
from collections import deque

# 백준 제출시 삭제
sys.stdin = open('input.txt', 'r')

# 공간 크기
N = int(input())
# 공간 정보 초기화
board = []
baby_row = -1
baby_col = -1
for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    
    if 9 in row:
        baby_row = i
        baby_col = row.index(9)

# 아기상어 상태 정보 초기화
baby_state = {
    'size' : 2, # 크기
    'position' : (baby_row, baby_col), # 위치
    'eat' : 0 # 먹은 물고기 수 (크기 변화 체크하려고)
}

board[baby_row][baby_col] = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 정답 시간
totalTime = 0

# 탐색 함수
def BFS(y, x):
    distance = [[-1] * N for _ in range(N)]
    queue = deque()

    distance[y][x] = 0 # 거리 저장
    queue.append((y, x))

    fish = [] # 먹을 수 있는 물고기 저장하는 배열
    MIN = float('inf')

    while queue:
        y, x = queue.popleft()

        if MIN < distance[y][x]:
            continue

        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            # 배열 경로 이탈
            if not (0 <= ny < N and 0 <= nx < N) :
                continue

            # 못지나감(이미방문/아기상어보다 큰 물고기)
            if distance[ny][nx] != -1 or board[ny][nx] > baby_state['size']:
                continue

            # 거리업뎃
            distance[ny][nx] = distance[y][x] + 1
                
            # 먹을 수 있는 물고기 셀
            if 0 < board[ny][nx] < baby_state['size'] :
                    fish.append([distance[ny][nx], ny, nx]) # 좌표와 거리(=먹을때 걸리는 시간) 저장
                    MIN = min(MIN, distance[ny][nx])
                
            queue.append((ny, nx))

    return fish

while True:
    # 아기상어 위치에서 BFS로 주변 물고기 탐색
    fish = BFS(baby_state['position'][0], baby_state['position'][1])
    
    # 거리 -> y좌표 -> x좌표대로 집어넣었으니까 sort 정렬만 해주면 됨
    fish.sort() 

    # 탐색했을 때 먹을 수 있는 물고기가 없으면 중지
    if len(fish) == 0:
        print(totalTime)
        break

    # 우선순위에 따라서 먹을 수 있는 물고기 먹기
    baby_state['eat'] += 1
    distance, y, x = fish[0]
    board[y][x] = 0
    totalTime += distance

    baby_state['position'] = (y, x)

    # 사이즈만큼 먹었으면 아기상어 크기 증가
    if baby_state['eat'] == baby_state['size']:
        baby_state['eat'] = 0
        baby_state['size'] += 1



