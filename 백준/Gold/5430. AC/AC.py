import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    P = input()
    n = int(input())
    arr_str = input()

    # 배열 입력 처리
    if arr_str == '[]':
        d = deque()
    else:
        d = deque(map(int, arr_str[1:-1].split(',')))

    is_reversed = False
    error_flag = False

    for p in P:
        if p == 'R':
            is_reversed = not is_reversed
        elif p == 'D':
            if not d:
                print("error")
                error_flag = True
                break
            if is_reversed:
                d.pop()
            else:
                d.popleft()

    if not error_flag:
        if is_reversed:
            d.reverse()
        print('[' + ','.join(map(str, d)) + ']')