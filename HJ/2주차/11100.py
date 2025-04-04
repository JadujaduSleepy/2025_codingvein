import sys
import heapq

N = int(sys.stdin.readline())

lst = [0]*N
for i in range(N):
    lst[i] = list(map(int, sys.stdin.readline().split()))

# 다음 강의는 시작시간을 들고 비교해야 하므로 시작시간 기준 정렬
lst.sort()

# 첫 번째 강의실에 가장 빠른 강의 하나 넣어줌
q = [lst[0][1]]    # 큐에 넣을 때 시작시간을 떼고 넣어 준다
# 이렇게 하면 강의가 끝나는 시간만 큐에 들어가서 이대로 정렬됨
for i in range(1, N):
    if q[0] <= lst[i][0]:    # 가장 빨리 끝나는 강의가 다음 강의 시작 시간보다 먼저 끝날 경우
        heapq.heappop(q)     # 이걸 빼고
        heapq.heappush(q, lst[i][1])    # 다음강의로 바꿔치기해준다
    else:
        heapq.heappush(q, lst[i][1])

print(len(q))