import sys
from collections import deque

# 백준 제출시 삭제
sys.stdin = open('input.txt', 'r')

# 수빈이가 있는 위치 N과 동생이 있는 위치 K
N, K = map(int, input().split())

MAX = 100000+1
t = 0
visited = [0] * (MAX+1)
queue = deque([[N,t]])

while queue :
    now_pos, now_time = queue.popleft()

    if (now_pos == K):
        print(now_time)
        break

    next_positions = [now_pos + 1, now_pos - 1, now_pos * 2]

    for next_pos in next_positions:
        if 0 <= next_pos < MAX and not visited[next_pos] : #유효한 범위
            visited[next_pos] = 1 
            queue.append([next_pos, now_time + 1])