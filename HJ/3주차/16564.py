import sys
input = sys.stdin.readline

n, k = map(int, input().split())
levels = [0]*n
for i in range(n):
    levels[i] = int(input())

levels.sort()

# x1을 x2까지 올리고, x1x2를 x3까지 올리고, ...
# diffs
diffs = [levels[i+1] - levels[i] for i in range(n-1)]


# cumulative differences = 현재까지 올린 모든 레벨
c_diff = 0
for idx, diff in enumerate(diffs):
    c_diff += (idx + 1) * diff  # 레벨 올리기
    if c_diff > k:    # 누적 값이 k보다 커질 경우
        r = k - c_diff + (idx + 1) * diff   # 남은 레벨
        t = levels[idx] + r // (idx + 1)
        break
else:   # 다 더해도 레벨이 남음
    r = k - c_diff
    t = levels[-1] + r // n

print(t)
