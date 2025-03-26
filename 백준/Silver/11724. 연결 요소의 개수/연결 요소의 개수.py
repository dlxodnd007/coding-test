import sys
sys.setrecursionlimit(int(1e6))
input = lambda : sys.stdin.readline().rstrip()

def dfs(node):
	global adj_list, visited, cnt

	if visited[node]:
		return

	visited[node] = True

	# print(node, end = ' ')

	for adj_node in adj_list[node]:
		dfs(adj_node)

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
		dfs(i)
		cnt += 1
print(cnt)