def solution(lottos, win_nums):
    zero = 0
    for num in lottos:
        zero += (num == 0)
        
    cnt = 0
    for num in lottos:
        cnt += (num in win_nums)
    
    cnt_to_rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    
    return [cnt_to_rank[cnt + zero], cnt_to_rank[cnt]]