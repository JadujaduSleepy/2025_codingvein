n = int(input())

if n % 2 == 1:
    print(0)
else:
    m = n // 2
    dp = [1]*(m+1)
    dp[1] = 3
    for i in range(2,m+1):
        dp[i] = 4*dp[i-1] - dp[i-2]
    print(dp[-1])