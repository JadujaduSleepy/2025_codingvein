# import sys를 사용하지 않으니 시간이 오래 걸려서... 
import sys
input = sys.stdin.readline

n = int(input())
std_list = []

# 입력. while (조건문) : => 조건문이 참일 때까지 빙글빙글 돈다 
while len(std_list)<n:
	name, lan_s, eng_s, math_s = input().split()
	lan_s = int(lan_s)
	eng_s = int(eng_s)
	math_s = int(math_s)
	std_list.append([name, lan_s, eng_s, math_s])

# 출력 
sorted_list = sorted(std_list, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range (0, n):
  print(sorted_list[i][0])