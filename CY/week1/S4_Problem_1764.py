import sys 
input = sys.stdin.readline 

# 듣못 n, 보못 m
n, m = map(int, input().split())
no_listen = []
no_see = []
no_all = []

# 이후 두 번째 줄부터 듣못 1~n+1 / 보못 n+2~ 끝까지 
# 중복 이름은 없음 
# 두 개에서 겹치는 이름의 수(list의 len)와 sorted() - 사전 순으로 출력해준다 

# 입력
while (len(no_listen)+len(no_see))< n+m :
	name = input()
	# 듣못 리스트가 n명보다 안차있으면 듣못에 넣어줌
	if len(no_listen)< n : 
		no_listen.append(name)
	# n명 +@ 찼으면 보못에 넣어줌 
	else : 
		no_see.append(name)
			
# 이중 포문 작성 시 시간 초과 발생 
# set 함수 사용하여 듣보 리스트 생성 
# 두 리스트의 교집합 찾기
no_all = list(set(no_listen) & set(no_see))
no_all = sorted(no_all)

print(len(no_all))
for i in no_all:
	print(i)