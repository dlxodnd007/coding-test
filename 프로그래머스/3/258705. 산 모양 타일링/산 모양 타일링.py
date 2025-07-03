def solution(n, tops):
    tops = [0] + tops
    
    dp = [0] * (n + 1)
    sub_dp = [0] * (n + 1)
    dp[0] = sub_dp[0] = 1
    
    for i in range(1, n + 1):
        if tops[i] == 0:
            sub_dp[i] = (dp[i - 1] + sub_dp[i - 1]) % 10007
        if tops[i] == 1:
            sub_dp[i] = (dp[i - 1] * 2 + sub_dp[i - 1]) % 10007
            
        dp[i] = (sub_dp[i] + dp[i - 1]) % 10007
    
    return dp[n]