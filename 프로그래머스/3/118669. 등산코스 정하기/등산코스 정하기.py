import sys
sys.setrecursionlimit(int(1e6))

def dfs(node, threshold):
    global n, paths, gates, summits, adj_list, visited, types, candidates
    
    # base case
    if visited[node]: return
    visited[node] = True
    
    if types[node] == 'summit':
        candidates.append(node)
        return
    
    # recursive case
    for nxt, w in adj_list[node]:
        if w <= threshold:
            dfs(nxt, threshold)

def solve(threshold): # intensity ≤ threshold 인 경우에 가능한 봉우리를 반환
    global n, paths, gates, summits, adj_list, visited, types, candidates
    candidates = []
    visited = [False] * (n + 1)
    
    for gate in gates:
        if not visited[gate]:
            dfs(gate, threshold)
            
    return candidates

def solution(_n, _paths, _gates, _summits):
    global n, paths, gates, summits, adj_list, visited, types, candidates
    n, paths, gates, summits = _n, _paths, _gates, _summits
    
    
    types = ['X'] * (n + 1)
    for gate in gates:
        types[gate] = 'gate'
    for summit in summits:
        types[summit] = 'summit'
        
    # 그래프 만들기
    adj_list = [[] for _ in range(n + 1)]
    for i, j, w in paths:
        adj_list[i].append((j, w))
        adj_list[j].append((i, w))
        
    # 파라메트릭 서치
    cur = 0
    step = int(1e7)
    while step != 0:
        while cur + step <= int(1e7) and len(solve(cur + step)) == 0: # [F, F, ..., F, (F), T, T, ..., T, T]
            cur += step
        step //= 2
    
    candidates = solve(cur + 1) # [F, F, ..., F, F, (T), T, ..., T, T]
    return min(candidates), cur + 1