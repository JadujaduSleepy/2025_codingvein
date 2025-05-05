import sys
input = sys.stdin.readline

n, k = map(int, input().split())

lst = [0]*n
for i in range(n):
    w, v = map(int, input().split())
    lst[i] = (w, v)

if n == 1: # 물건이 1개면
    # 물건이 가방보다 무거울 때
    if k < lst[0][0]:
        print(0)
    else:
        print(lst[0][1])
    
else:
    # dp테이블 - 가로: 가방 무게, 세로: 물건 번호
    dp = [[0]*(k+1) for _ in range(n)]


    for idx, (wi, vi) in enumerate(lst):
        for j in range(k+1):
            # 가방 무게가 j고 물건이 j보다 무거우면 못 넣음 => 가치 그대로
            if j < wi:
                dp[idx][j] = dp[idx-1][j]
            else:   # 넣을 수 있을 때에는 가치 비교
                dp[idx][j] = max(dp[idx-1][j], dp[idx-1][j-wi]+vi)

    print(max(dp)[-1])