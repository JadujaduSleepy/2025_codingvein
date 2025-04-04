# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이

import sys

# 백준 제출시 삭제
sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for _ in range(n)]

def solution() :
    counter = dict()
    
    #산술평균
    print(int(round(sum(data)/n, 0)))

    #중앙값
    data.sort()
    print(data[n//2])

    #최빈값
    for i in range(n):
        # 값 존재하면 +1 없으면 1 초기화
        counter[data[i]] = counter.get(data[i], 0) + 1
    max_count = max(counter.values())
    # 최빈값의 최댓값과 같은 key를 배열로 추출
    temp = [n for n, m in counter.items() if max_count == m]
    # 최빈값 2개 이상이면 두번째로 작은거 출력
    print(temp[1] if len(temp) > 1 else temp[0])

    #범위
    print(abs(data[0] - data[-1]))

if __name__ == "__main__":
    solution()