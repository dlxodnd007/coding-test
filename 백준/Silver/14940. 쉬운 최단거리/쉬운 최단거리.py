import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

def bfs(sy, sx):
	global dy, dx, n, m, matrix, result_matrix

	visited = [[False] * m for _ in range(n)]

	q = deque()
	q.append([0, sy, sx])
	visited[sy][sx] = True
	result_matrix[sy][sx] = 0

	while q:
		dist, y, x = q.popleft()

		for i in range(4):
			ny = y + dy[i]
			nx = x + dx[i]

			if (0 <= ny <= n -1 and 0 <= nx <= m - 1) and (not visited[ny][nx]) and (matrix[ny][nx] != 0):
				q.append([dist + 1, ny, nx])
				visited[ny][nx] = True
				result_matrix[ny][nx] = dist + 1



n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
result_matrix = [[-1 for _ in range(m)] for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for y in range(n):
    for x in range(m):
        if matrix[y][x] == 0:
            result_matrix[y][x] = 0
        elif matrix[y][x] == 2:
            bfs(y, x)

for row in result_matrix:
	print(* row)