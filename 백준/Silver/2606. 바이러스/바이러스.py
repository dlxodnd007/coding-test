def solve_dfs(node):
	global adj_list, visited_dfs, cnt

	if visited_dfs[node]:
		return
	visited_dfs[node] = True
	
	cnt += 1
	# print(node, end = ' ')

	for adj_node in adj_list[node]:
		solve_dfs(adj_node)

N = int(input())
M = int(input())

adj_list = [[] for _ in range(N + 1)]

for _ in range(M):
	a, b = map(int, input().split())
	adj_list[a].append(b)
	adj_list[b].append(a)

visited_dfs = [False] * (N + 1)

cnt = 0
solve_dfs(1)
print(cnt - 1)