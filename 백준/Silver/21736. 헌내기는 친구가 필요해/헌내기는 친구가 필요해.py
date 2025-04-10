import sys
sys.setrecursionlimit(10**6)
from collections import deque

def bfs(y, x):
	global N, M, matrix, visited, dy, dx, ans

	q = deque()
	q.append((y, x))
	visited[y][x] = True

	while q:
		y, x = q.popleft()

		if matrix[y][x] == "P":
			ans += 1

		for i in range(4):
			ny = dy[i] + y
			nx = dx[i] + x
			if (0 <= ny < N) and (0 <= nx < M) and (matrix[ny][nx] != 'X') and (not visited[ny][nx]):
				q.append((ny, nx))
				visited[ny][nx] = True


N , M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
ans = 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


for y in range(N):
	for x in range(M):
		if matrix[y][x] == "I":
			bfs(y, x)
			break
print(ans if ans != 0 else "TT")
