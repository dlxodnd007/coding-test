def solution(coin, cards):
    n = len(cards)
    pair = [-1] * n # pair[x]: 카드 x의 짝의 인덱스
    cost = [-1] * n # cost[x]: 카드 x를(x와 x에 대한 쌍을) 얻기 위해 지불해야 하는 코인의 수
    
    # 짝 정보(pair) 갱신
    for b in range(n - 1, -1, -1):
        if pair[b] != -1: continue
        for a in range(b):
            if cards[a] + cards[b] == n + 1: # a와 b가 짝이면
                cost[b] = 2
                pair[a] = b
                pair[b] = a
    
    # 처음 n/3 장의 카드의 cost를 깎기
    for idx in range(n // 3):
        if idx < pair[idx]:
            cost[pair[idx]] -= 1
        else:
            cost[idx] -= 1
    
    # 답 구하기
    choosed = [False] * n
    pair_cnt = 0
    while coin >= 0:
        max_idx = n // 3 + 2 * (pair_cnt + 1) - 1 # 게임이 끝나지 않고 갈 수 있는 최대 인덱스
        max_idx = min(max_idx, n - 1)
        
        best_idx = -1
        for idx in range(max_idx + 1):
            if choosed[idx] or idx < pair[idx]: # 고른 카드거나, 앞에 있는 카드면
                continue
            if best_idx == -1 or cost[idx] < cost[best_idx]: # 더 좋은 선택지가 있으면 갱신
                best_idx = idx
        
        if best_idx == -1 or coin - cost[best_idx] < 0: # 모든 카드를 골랐거나, 코인이 부족하면
            break
            
        coin -= cost[best_idx]
        choosed[best_idx] = True
        pair_cnt += 1
    
    return min(pair_cnt + 1, n // 3 + 1) # n // 3 + 1 은 최대로 나올 수 있는 라운드를 의미
