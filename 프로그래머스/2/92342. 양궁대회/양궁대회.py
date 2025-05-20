from itertools import combinations_with_replacement

def get_cur_point(apeach, lion):
    apeach_point = 0
    lion_point = 0
    
    for i in range(11):
        if apeach[i] == 0 and lion[i] == 0:
            continue
        if apeach[i] >= lion[i]:
            apeach_point += 10 - i
        else:
            lion_point += 10 - i
            
    return lion_point - apeach_point        


def solution(n, info):
    best_point = 0
    best_result = [0] * 11
    
    for comb in combinations_with_replacement(range(11), n):
        cur_result = [0] * 11
        
        for num in comb:
            cur_result[num] += 1
            
        cur_point = get_cur_point(info, cur_result)
        if (cur_point > best_point) or (cur_point == best_point and cur_result[::-1] > best_result[::-1]):
            best_point = cur_point
            best_result = cur_result[:]
    
    return ([-1] if best_point == 0 else best_result)