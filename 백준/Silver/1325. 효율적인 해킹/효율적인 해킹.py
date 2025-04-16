import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

def bfs(node):
    visited = [False] * (N + 1)
    visited[node] = True
    q = deque([node])
    cnt = 1

    while q:
        node = q.popleft()

        for adj_node in adj_list[node]:
            if not visited[adj_node]:
                visited[adj_node] = True
                q.append(adj_node)
                cnt += 1

    return cnt

N, M = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]
cnt_list = [0] * (N + 1)
max_cnt = 0

for _ in range(M):
	a, b = map(int, input().split())
	adj_list[b].append(a)

for i in range(1, N + 1):
    cnt_list[i] = bfs(i)
    max_cnt = max(max_cnt, cnt_list[i])

for i in range(1, N + 1):
    if cnt_list[i] == max_cnt:
        print(i, end=' ')