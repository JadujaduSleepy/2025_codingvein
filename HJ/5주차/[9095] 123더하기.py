import sys
input = sys.stdin.readline


# 각 문자열은 덧셈 기호를 생략한 조합을 나타냄.. 111=1+1+1
# 3까지 미리 정의
dp = {i:set() for i in range(1,11)}
dp[1] = set(['1'])
dp[2] = set(['11', '2'])
dp[3] = set(['111', '12', '21', '3'])

# 나머지 10까지 채우기
for n in range(4, 11):
    dp[n].add('1'*n)
    for com in dp[n-1]:
        lst = list(map(int, list(com)))
        # lst = [1,1,1], [1, 2], ...
        for i in range(len(lst)):
            tmp = lst.copy()
            # tmp = [2,1,1] or [1,2,1] or [1,1,2]
            # 각 자리별로 하나씩만 1을 더함
            tmp[i] = lst[i] + 1
            if tmp[i] < 4:
                dp[n].add(''.join(map(str, tmp)))



t = int(input())

test = [0]*t
for i in range(t):
    test[i] = int(input())

for i in range(t):
    print(len(dp[test[i]]))
