import sys
input = sys.stdin.readline

n, k = map(int, input().split()) 
# root : n (시작) 

from collections import deque

def bfs(n, k):
    if n>=k: # 1칸씩 빠꾸밖에 못함 
        return n-k # 되빠꾸 초         
    # 방문 여부 체크 배열 100,000개 만들어야됨..?? 
    visited = [False]*100001 # 늘 1개 더만듬 
    
    que = deque()
    que.append((n, 0)) # 시작 노드 넣고 시간도 옆에 같이 저장해주었다 
    visited[n] = True # 방문 처리하고 
    
    while que: 
        # 현재 위치랑 시간을 pop하고 
        now, time = que.popleft() 
        if now == k :
           return time
        
        # 인접 노드가 세 개인데 now-1, now+1, now*2 이렇게 있는 거고 
        # 이 세 개를 계산해서 넣어주는 거
        # now - 1 
        # 방문 안했고 + > 이것도 추가 : 지정 범위 안에 있으면 
        if (0 <= now-1<= 100000) and not visited[now-1]:
            que.append((now-1, time+1)) # 추가 
            visited[now-1]=True # 방문 처리 
        
        # now + 1 
        # 방문 안했고 + > 이것도 추가 : 지정 범위 안에 있으면 
        if (0 <= now+1<= 100000) and not visited[now+1]:
            que.append((now+1, time+1)) # 추가 
            visited[now+1]=True # 방문 처리 
        
        # now * 2 
        # 방문 안했고 + > 이것도 추가 : 지정 범위 안에 있으면 
        if (0 <= now*2<= 100000) and not visited[now*2]:
            que.append((now*2, time+1)) # 추가 
            visited[now*2]=True # 방문 처리 
            
        # 이거 위에 세 개 합치는 법이 있을텐데 머리가 멎어서 전부 다 써버렸다 

print(bfs(n, k))