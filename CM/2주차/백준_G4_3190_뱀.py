import sys

arr = list(map(int, input().strip().split( )))
# 게임판 보드 칸 수
N = arr[0] 
arr = list(map(int, input().strip().split( )))

# 사과의 개수
K = arr[0]
# 사과 위치 배열
apple = [list(map(int, input().strip().split( ))) for _ in range(K)]
arr = list(map(int, input().strip().split( )))

# 뱀 이동 횟수
L = arr[0]

# 뱀 이동 목록
move = [list(map(str, input().strip().split( ))) for _ in range(L)]
for i in range(L) :
    move[i][0] = int(move[i][0])

def snake_move(head, now) : # 다음 머리의 위치 좌표를 return
    x = now[0]
    y = now[1]
    if (head == 0) : #북
        return [x-1, y]
    elif (head == 1) : #동
        return [x, y+1]
    elif (head == 2) : #남
        return [x+1, y]
    else : #서
        return [x, y-1]

def solution(N, K, L, apple, move) :

    count = 1 # 게임 시작 이후 경과한 초
    finish = 0 # 게임 상태 0 = 진행 / 1 = 게임 오버
    head = 1 # 뱀 진행 방향 -> 북 = 0 / 동 = 1 / 남 = 2 / 서 = 3
    snake = [[0,0]] #뱀 위치를 저장하는 배열 (큐) 꼬리 ... 머리
    board = [[0 for j in range(N)] for i in range(N)] # 게임판 보드
    # 비어있는 칸 = 0 / 뱀 = 1 / 사과 = 2
    board[0][0] = 1 # 태초의 뱀
    for x, y in apple: # 보드에 사과 깔기
        board[x-1][y-1] = 2
    
    while not(finish) : #게임 끝날때까지 반복
        
        next = snake_move(head, snake[-1]) #다음머리
        # print("next : ",next)
        # print("snake : ", snake)
        #벽인지 확인
        if (next[0] >= N or next[1] >= N or next[0] < 0 or next[1] < 0) :
            break
        #몸에 부딪히는지 확인
        if (next in snake) :
            break
        
        #문제 없음
        snake.append(next)

        if (board[snake[-1][0]][snake[-1][1]] == 2) : #머리 부분에 사과 있으면
            board[snake[-1][0]][snake[-1][1]] = 1 #뱀 놓음
            #길이 늘어남
        elif (board[snake[-1][0]][snake[-1][1]] == 0) : #사과없음
            board[snake[-1][0]][snake[-1][1]] = 1 #뱀 놓음
            board[snake[0][0]][snake[0][1]] = 0
            snake.pop(0)
            
        board[snake[-1][0]][snake[-1][1]] = 1 #보드에 뱀 기록
        

        #마지막에 머리 방향 변경
        if (move) :
            if (count == move[0][0]) : #현재 진행 시간에 뱀 움직임이 있을 경우
                if (move[0][1] == 'D') : #오른쪽 90도
                    head = head + 1
                else : #왼쪽 90도
                    head = head - 1
                if (head < 0) :
                    head = 3
                if (head > 3) :
                    head = 0
                move.pop(0) #move 배열 첫번째 제거

        # print(count, "초 끝")
        # print("-----------------")
        # for i in board : 
        #     print(i)
        # print("-----------------")

        count = count + 1

    return count

print(solution(N, K, L, apple, move))