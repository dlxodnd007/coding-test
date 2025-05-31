from collections import deque

def solution(info, edges):
    
    N = len(info)
    
    adj_list = [[] for _ in range(N)]
    for a,b in edges:
        adj_list[a].append(b)
        adj_list[b].append(a)
        
    ans = 0
    q = deque()
    q.append(({0}, 1, 0))
    
    while q:
        cur_set, cur_sheep, cur_wolf = q.popleft()
        ans = max(ans, cur_sheep)
        
        nxt_nodes = set()
        for node in cur_set:
            for adj_node in adj_list[node]:
                if adj_node not in cur_set:
                    nxt_nodes.add(adj_node)
                    
        for node in nxt_nodes:
            if info[node] == 0:
                q.append((cur_set | {node}, cur_sheep + 1, cur_wolf))
            elif info[node] == 1 and cur_sheep > cur_wolf + 1:
                q.append((cur_set | {node}, cur_sheep, cur_wolf + 1))

    return ans