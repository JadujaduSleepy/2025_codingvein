import sys
N = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for i in range(N)]

# 일단 정렬하시오
data.sort()

M, m= data[-1], data[0]

# 산술평균 mean()
mean = sum(data)/N

# 중앙값
median = data[int(N/2)]

# 최빈값
## 등장빈도 count
nums = [0]*(M-m+1)
for i in range(len(data)):
    nums[data[i]-m] += 1

# 가장 많이 등장하는 횟수 
max_count = max(nums)

# 세면서 max값과 일치하는지 체크
# 가장 먼저 만난 값을 일단 mode에 기록
# 진행하다가 한 번 더 만났다면 그 값을 mode에 덮어씌운 후 종료
for i in range(len(nums)):
    if nums[i] == max_count:
        mode = i + m
        idx = i
        break
# 기록한 idx 다음부터 재시작
for j in range(idx + 1, len(nums)):
    if nums[j] == max_count:
        mode = j + m
        break

# 범위 : max-min
rng = M-m

print(round(mean))
print(median)
print(mode)
print(rng)


# # 최빈값 부분을 아래처럼 해봤는데 이건 틀렸대 왜일까?
# try:
#     mode = nums.index(max_count, 2) + m
# except ValueError:
# # 최빈값이 하나인 경우에는 index(,2)에서 ValueError가 발생하므로 예외처리
#     mode = nums.index(max_count) + m