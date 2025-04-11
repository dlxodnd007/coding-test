import sys
input = lambda : sys.stdin.readline().rstrip()

def get_sum(sy, sx, ey, ex):
	global matrix, psum
	return psum[ey][ex] - (psum[ey][sx - 1] + psum[sy - 1][ex] - psum[sy - 1][sx - 1])

N, M = map(int, input().split())
matrix = [[0] * (N + 1)]
psum = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(N):
	matrix += [[0] + list(map(int, input().split()))]

for i in range(1, N + 1):
	for j in range(1, N + 1):
		psum[i][j] = psum[i - 1][j] + psum[i][j - 1] - psum[i - 1][j - 1] + matrix[i][j]

for _ in range(M):
	x1, y1, x2, y2 = map(int, input().split())
	print(get_sum(x1, y1, x2, y2))
