from collections import deque

def solution(queue1, queue2):
    main_que, sub_que = deque(queue1), deque(queue2)
    
    total = sum(main_que + sub_que)
    if total % 2 == 1:
        return -1
    target = total // 2
    
    # 200만 번 그리디하게 시뮬레이션 수행
    main_sum = sum(main_que)
    for cnt in range(0, int(2e6)):
        if main_sum == target: return cnt
        elif main_sum < target: # sub_que → main_que
            val = sub_que.popleft()
            main_sum += val
            main_que.append(val)
        elif main_sum > target: # main_que → sub_que
            val = main_que.popleft()
            main_sum -= val
            sub_que.append(val)
            
    return -1