from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N, M = map(int, input().split())
matrix = ['0' * (M + 1)] + ['0' + input() for _ in range(N)]

q = deque()
visited = [[False] * (M + 1) for _ in range(N + 1)]

q.append([1, 1, 1])
visited[1][1] = True

while q:
	dist, y, x = q.popleft()

	if y == N and x == M:
		print(dist)
		exit()

	for i in range(4):
		ny = y + dy[i]
		nx = x + dx[i]

		if (1 <= ny <= N and 1 <= nx <= M) and (not visited[ny][nx]) and (matrix[ny][nx] == '1'):
			q.append([dist + 1, ny, nx])
			visited[ny][nx] = True
print(-1)