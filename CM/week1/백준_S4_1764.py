import sys

# 백준 제출시 삭제
sys.stdin = open('input.txt', 'r')
n, m = map(int, input().split())

듣도_못한_사람 = set()
보도_못한_사람 = set()

for _ in range(n):
    듣도_못한_사람.add(input())

for _ in range(m):
    보도_못한_사람.add(input())

# 교집합
듣보잡 = 듣도_못한_사람 & 보도_못한_사람

# 정렬
듣보잡_리스트 = sorted(list(듣보잡))

# 결과 출력
print(len(듣보잡_리스트))
for 이름 in 듣보잡_리스트:
    print(이름)