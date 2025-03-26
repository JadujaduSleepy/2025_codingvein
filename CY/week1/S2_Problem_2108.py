import sys 
input = sys.stdin.readline

# N 받기. 단, 홀수임 
num = int(input()) 
num_list = []
while len(num_list) < num : 
	num_list.append(int(input()))

# 오름차순 정렬 
num_list.sort()

# 입력 & 출력 
# 첫째 줄 - 산술평균 > 이후 round 
avg = sum(num_list)/num
print(round(avg))

# 둘째 줄 - 중앙값
med = num_list[(num-1)//2]
print(med)

# 셋째 줄 - 최빈값. 여러 개 일시 두 번째로 작은 값. 
# num_count라는 dict에 저장 
# key(num_list의 값) : item (횟수) 
num_count = {}
for i in range (0, num) : 
	num_count[num_list[i]]=num_list.count(num_list[i])

time = max(num_count.values())
final=[]

for key, value in num_count.items() :
	if value == time:
		final.append(key)

if len(final)<2:
	print(final[0])
else:
	final.sort()
	print(final[1])


# 넷째 줄 - 범위 
rng = num_list[num - 1] - num_list[0]
print(rng)