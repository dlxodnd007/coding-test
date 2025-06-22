from itertools import combinations

def get_win_num(comb1, comb2): # A가 comb1, B가 comb2일 때, A가 이기는 횟수 반환
    global N, dice
    
    # dp1[n][x]: comb1의 n번째 주사위까지 살펴봤을 때, 점수의 합이 x가 나오는 경우의 수
    dp1 = [[0] * (501) for _ in range(N + 1)]
    dp1[0][0] = 1
    # dp2[n][x]: comb2의 n번째 주사위까지 살펴봤을 때, 점수의 합이 x가 나오는 경우의 수
    dp2 = [[0] * (501) for _ in range(N + 1)]
    dp2[0][0] = 1
    
    for n in range(1, N + 1):
        for x in range(1, 501):
            # dp1[n][x], dice[comb1[n - 1]]
            for num in dice[comb1[n - 1]]:
                if x - num >= 0:
                    dp1[n][x] += dp1[n - 1][x - num]
                
            # dp2[n][x], dice[comb2[n - 1]]
            for num in dice[comb2[n - 1]]:
                if x - num >= 0:
                    dp2[n][x] += dp2[n - 1][x - num]
    
    # O(500 * 500)
    win_num = 0
    for x in range(1, 501): # when player1 score is x
        for i in range(1, x): # when player2 score is y
            win_num += (dp1[N][x] * dp2[N][i])

    return win_num

def solution(_dice):
    global N, dice
    dice = _dice
    N = len(dice) // 2
    
    best_win_num = -1
    best_comb = None
    for cur_comb in combinations(range(N * 2), N): # range(N * 2) = (0, 1, 2, 3, 4, 5)
        sub_comb =  tuple(sorted(list(set(range(N * 2)) - set(cur_comb))))
         # cur_comb = (0, 3, 4)
         # sub_comb = (1, 2, 5)
        
        cur_win_num = get_win_num(cur_comb, sub_comb)
        if cur_win_num > best_win_num:
            best_win_num = cur_win_num
            best_comb = list(cur_comb) # deepcopy
            
    return [bc + 1 for bc in best_comb]