from collections import deque

def bfs(sy, sx):
	global N, matrix, visited, dy, dx

	q = deque()
	q.append([sy, sx])
	visited[sy][sx] = True

	while q:
		y, x = q.popleft()

		for i in range(4):
			ny = y + dy[i]
			nx = x + dx[i]

			if (0 <= ny < N and 0 <= nx < N) and (not visited[ny][nx]) and (matrix[ny][nx] == matrix[y][x]):
				q.append([ny, nx])
				visited[ny][nx] = True

N = int(input())
matrix = [list(input().strip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
count_normal = 0
count_colorblind = 0


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for y in range(N):
	for x in range(N):
		if not visited[y][x]:
			bfs(y, x)
			count_normal += 1

for y in range(N):
	for x in range(N):
		if matrix[y][x] == 'G' or matrix[y][x] == 'R':
			matrix[y][x] = 'C' # common

visited = [[False] * N for _ in range(N)]

for y in range(N):
	for x in range(N):
		if not visited[y][x]:
			bfs(y, x)
			count_colorblind += 1

print(count_normal, count_colorblind)