from collections import deque

def solution(rc, operations):
    left_dq = deque([r[0] for r in rc])
    right_dq = deque([r[-1] for r in rc])
    mid_dqs = deque([deque(r[1:-1]) for r in rc])
    
    for op in operations:
        if op == 'ShiftRow':
            left_dq.appendleft(left_dq.pop())
            right_dq.appendleft(right_dq.pop())
            mid_dqs.appendleft(mid_dqs.pop())
        else: # Rotate
            mid_dqs[0].appendleft(left_dq.popleft())
            right_dq.appendleft(mid_dqs[0].pop())
            mid_dqs[-1].append(right_dq.pop())
            left_dq.append(mid_dqs[-1].popleft())
    
    return [[left_dq[i]] + list(mid_dqs[i]) + [right_dq[i]] for i in range(len(rc))]
