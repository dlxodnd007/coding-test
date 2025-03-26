import sys
from collections import deque
sys.setrecursionlimit(int(1e6))
input = lambda : sys.stdin.readline().rstrip()
def bfs(snode):
	global adj_list, visited

	q = deque()
	q.append(snode)
	visited[snode] = True

	while q:
		node = q.popleft()

		for adj_node in adj_list[node]:
			if visited[adj_node]:
				continue
			q.append(adj_node)
			visited[adj_node] = True

N, M = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]

for _ in range(M):
	a, b = map(int, input().split())
	adj_list[a].append(b)
	adj_list[b].append(a)

visited = [False] * (N + 1)
cnt = 0

for i in range(1, N + 1):
	if not visited[i]:
		bfs(i)
		cnt += 1

print(cnt)