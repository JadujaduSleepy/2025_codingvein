import sys 
# heap 사용 
import heapq
input = sys.stdin.readline

num = int(input()) # N 
classes = [] # 강의 리스트 

# full 입력 
for x in range (num): 
    s, t = map(int, input().split()) 
    classes.append([s, t])
    # Si 순서대로 정렬 
    
classes.sort(key=lambda classes : classes[0])


count = 1
ts = [] # t들 heap
heapq.heappush(ts, classes[0][1]) # 넣어주기 
for x in range (1, num) : 
    # classes[x][0] : S / classes[x][1] : T 
    if classes[x][0] >= ts[0] : 
        heapq.heappop(ts)
        heapq.heappush(ts, classes[x][1]) # Ti push 
    else :
        count += 1
        heapq.heappush(ts, classes[x][1])

print(count)