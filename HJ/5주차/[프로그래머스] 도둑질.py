def solution(money):

    #첫 번째 집을 터는 경우
    dp = [0]*(len(money)-1)
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])
    for i in range(2, len(money)-1):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])
    
    result1 = dp[-1]
        
    #첫 번째 집을 안 터는 경우
    dp = [0]*(len(money)-1)     # 재사용하기 => 초기화
    dp[0] = money[1]    # 한 칸 밀어서 시작
    dp[1] = max(money[1], money[2])
    for i in range(3, len(money)):
        dp[i-1] = max(dp[i-2], dp[i-3] + money[i])

    result2 = dp[-1]

    return max(result1, result2)    # 두 case 중 더 큰 값을 리턴