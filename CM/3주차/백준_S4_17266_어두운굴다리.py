#어두운굴다리 45396KB 88ms

import sys

# 백준 제출시 삭제
sys.stdin = open('input.txt', 'r')

# 굴다리 길이 N 입력받기
N = int(input())
# 가로등 개수 M 입력받기
M = int(input())
# 가로등 위치 x 입력받기
lamp_positions = list(map(int, input().split()))

# 제일 첫번째 램프랑 시작점 사이 거리
n1 = lamp_positions[0] - 0
# 마지막 램프랑 끝 사이 거리
n2 = N - lamp_positions[-1]

max_height = 0;

# 램프 사이사이를 봅니다
for i in range(M-1):
    간격절반, 나머지 = divmod(lamp_positions[i+1] - lamp_positions[i], 2)
    max_height = max(max_height, 간격절반 + 나머지)

answer = max(n1, n2, max_height)

print(answer)