import sys

# 입력부분
n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

## 틀렸습니다!!
## 이건 눈덩이를 중복으로 쓰게 돼서 그럼

# 리스트 초기화 -> choose(n, 2)개 만큼
sums_len = int(n*(n-1)/2)
sums = [0]*sums_len

# 가능한 합의 모든 경우를 기록
count = 0   # 인덱스
for i in range(len(lst)):   
    for j in range(i+1, len(lst)):
        sums[count] = lst[i] + lst[j]
        count += 1

sums.sort()

# sums안에 들어 있는 합의 차이들을 기록
diffs = [0]*int(sums_len-1)

for i in range(sums_len-1):
    diffs[i] = sums[i+1] - sums[i]

diffs.sort()

# 가장 작은 차이 출력
print(diffs[0])