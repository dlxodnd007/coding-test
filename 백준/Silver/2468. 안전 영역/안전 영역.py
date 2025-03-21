import sys
sys.setrecursionlimit(int(1e6))

from collections import deque

def bfs(y, x, h):
	global dy, dx, N, matrix, visited

	q = deque()
	q.append([y, x])
	visited[y][x] = True

	while q:
		y, x = q.popleft()

		for i in range(4):
			ny = y + dy[i]
			nx = x + dx[i]
			if (0 <= ny < N and 0 <= nx < N) and (not visited[ny][nx]) and (matrix[ny][nx] > h):
				q.append([ny, nx])
				visited[ny][nx] = True


def get_num_bfs(height):
	global dy, dx, N, matrix, visited

	visited = [[False] * N for _ in range(N)]

	num = 0
	for y in range(N):
		for x in range(N):
			if (not visited[y][x]) and (matrix[y][x] > height):
				bfs(y, x, height)
				num += 1

	return num


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for h in range(101):
	ans = max(ans, get_num_bfs(h))

print(ans)