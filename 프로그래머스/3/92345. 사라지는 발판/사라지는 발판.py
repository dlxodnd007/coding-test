from copy import deepcopy

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def in_range(y, x):
    global R, C
    return (0 <= y < R and 0 <= x < C)

def func(board, cury, curx, opy, opx):  # 현재 상태에서 최적의 게임을 했을 때 (결과, 최대 이동횟수)
    global R, C
    
    # base case
    if not in_range(cury, curx) or board[cury][curx] == 0:
        return (False, 0)
    if not in_range(opy, opx) or board[opy][opx] == 0:
        return (True, 0)
    
    cnt = 0
    for i in range(4):
        ny = cury + dy[i]
        nx = curx + dx[i]
        cnt += (not in_range(ny, nx) or board[ny][nx] == 0)
    if cnt == 4:
        return (False, 0)
    
     # recursive case
    cboard = deepcopy(board)
    cboard[cury][curx] = 0
        
    win_case = []
    lose_case = []
    for i in range(4):
        ny = cury + dy[i]
        nx = curx + dx[i]
        nres, ncnt = func(cboard, opy, opx, ny, nx)
        if nres == False:
            win_case.append(ncnt)
        else:
            lose_case.append(ncnt)
            
    if win_case: # 이기는 경우가 있다면, 최대한 빨리 이겨야 함.
        return (True, min(win_case) + 1)
    else: # 이기는 경우가 없다면, 최대한 오래 버티도록 해야 함.
        return (False, max(lose_case) + 1)

def solution(board, aloc, bloc):
    global R, C
    R = len(board)
    C = len(board[0])

    return func(board, *aloc, *bloc)[1]