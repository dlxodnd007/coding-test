INF = int(1e12)

def solution(alp, cop, problems):
    problems.append([0, 0, 1, 0, 1])
    problems.append([0, 0, 0, 1, 1])
    
    target_alp = max([problem[0] for problem in problems] + [alp])
    target_cop = max([problem[1] for problem in problems] + [cop])
    
    # solve (dp : bottom up)
    dp = [[INF] * (target_cop + 1) for _ in range(target_alp + 1)]
    dp[alp][cop] = 0
    
    for ap in range(alp, target_alp + 1):
        for cp in range(cop, target_cop + 1):
            for aq, cq, ad, cd, cost in problems:
                if ap >= aq and cp >= cq:
                    nxt_ap = min(target_alp, ap + ad)
                    nxt_cp = min(target_cop, cp + cd)
                    dp[nxt_ap][nxt_cp] = min(dp[nxt_ap][nxt_cp], dp[ap][cp] + cost)
                    
    return dp[target_alp][target_cop]