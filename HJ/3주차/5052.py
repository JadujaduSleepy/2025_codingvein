import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    nums = [input().rstrip() for _ in range(n)]
    # 텍스트인 상태로 정렬 => 그래야 '113'을 포함하는 번호가 있을 경우 '11245' '113' '11345' 처럼 나온다
    nums.sort()
    for i in range(n-1):    # i+1번째까지 보므로 - 1
        if nums[i] == nums[i+1][:len(nums[i])]:
            print("NO")
            break
    else:
        print("YES")

        