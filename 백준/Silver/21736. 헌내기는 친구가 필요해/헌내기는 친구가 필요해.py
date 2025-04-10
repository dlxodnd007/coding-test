import sys
sys.setrecursionlimit(10**6)

def dfs(y, x):
	global N, M, matrix, visited, dy, dx, ans

	if visited[y][x]:
		return

	if matrix[y][x] == "P":
		ans += 1

	visited[y][x] = True

	for i in range(4):
		ny = dy[i] + y
		nx = dx[i] + x
		
		if (0 <= ny < N) and (0 <= nx < M) and (matrix[ny][nx] != 'X') and (not visited[ny][nx]):
			dfs(ny, nx)

N , M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
ans = 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


found = False
for y in range(N):
	for x in range(M):
		if matrix[y][x] == "I":
			dfs(y, x)
			found = True
			break
	if found:
		break

print(ans if ans != 0 else "TT")