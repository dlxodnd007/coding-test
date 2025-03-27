import sys
sys.setrecursionlimit(int(1e9))

def dfs(y, x):
	global dy, dx, M, N, K, adj_list, visited

	if not (0 <= y < N and 0 <= x < M):
		return
	if visited[y][x] or adj_list[y][x] != 1:
		return

	visited[y][x] = True

	for i in range(4):
		ny = y + dy[i]
		nx = x + dx[i]
		dfs(ny, nx)

def get_num():
	global dy, dx, M, N, K, adj_list, visited

	visited = [[False] * M for _ in range(N)]
	cnt = 0

	for y in range(N):
		for x in range(M):
			if visited[y][x]:
				continue
			if adj_list[y][x] == 1:
				dfs(y, x)
				cnt += 1

	return cnt

T = int(input())

for _ in range(T):

	M, N, K = map(int, input().split())
	adj_list = [[0] * M for _ in range(N)]

	dy = [1, 0, -1, 0]
	dx = [0, 1, 0, -1]

	for _ in  range(K):

		x, y = map(int, input().split())
		adj_list[y][x] = 1

	print(get_num())