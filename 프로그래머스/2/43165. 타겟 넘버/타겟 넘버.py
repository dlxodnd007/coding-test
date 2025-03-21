from collections import deque

def solution(numbers, target):
    answer = 0
    N = len(numbers)
    
    q = deque()
    q.append([0, 0, 0])
    
    while q:
        dist, cur_sum, pos = q.popleft()
        
        if dist == N:
            if cur_sum == target:
                answer += 1
            continue            
        
        for nxt_num in [numbers[pos], -numbers[pos]]:
                q.append([dist + 1, cur_sum + nxt_num, pos + 1])
                
    
    return answer