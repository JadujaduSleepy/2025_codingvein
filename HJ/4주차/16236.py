import sys
input = sys.stdin.readline

from collections import deque


n = int(input())
q = deque()
arr = [0]*n
for i in range(n):
    arr[i] = list(map(int, input().split()))
    for j in range(n):
        if arr[i][j] == 9:
            q.append((i, j, 0))

curr_size = 2
eat = 0

# 물고기 하나 먹기
def bfs():

    global curr_size
    global eat

    dy = (-1, 0, 0, 1)
    dx = (0, -1, 1, 0)

    while q:

        y, x, t = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if not (0 <= ny < n and 0 <= nx < n):
                continue

            if arr[ny][nx] > curr_size:    # 못 지나가는 경우 => 지금 크기보다 클 때
                continue

            # 물고기 먹기
            # 지금 상어 위치와 가장 가까운 먹을 수 있는 물고기 집합을 구한 후 기준에 따라 정렬해야 함..
            ## 근데 더 이상 모르겠다

            if arr[ny][nx] >= 1 and arr[ny][nx] <= 6 and arr[ny][nx] < curr_size:
                q.appendleft((ny, nx, t+1))   # 현재 위치 다시 큐에 추가

                eat += 1
                if eat >= curr_size:
                    curr_size += 1
                    eat = 0
                
                return t+1
            
            # 그냥 지나가는 길 -> 0이거나 지금 사이즈와 같은 물고기
            if not arr[ny][nx]:
                arr[ny][nx] = 9
                q.append((ny, nx, t+1))
                
            elif arr[ny][nx] <= 6 and arr[ny][nx] == curr_size:
                q.append((ny, nx, t+1))


result = 0

while True:    

    all_fishes = [fish for fish in sum(arr, []) if fish > 0]    # 남은 물고기들의 크기
    if all(fish >= curr_size for fish in all_fishes):
        break

    result = bfs()

    # 다시 실행하기 전에 큐와 지나간 자리를 초기화해야 됨
    q = deque([q[0]])
    # 지나간 자리 초기화
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 9:
                arr[i][j] = 0
    arr[q[0][0]][q[0][1]] = 9    # 먹은 자리 9로 만들기

print(result)
    