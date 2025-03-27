from collections import deque

INF = int(1e12)

M, N, H = map(int, input().split())
matrix = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

q = deque()
time = [[[INF] * M for _ in range(N)] for _ in range(H)]

for h in range(H):
	for y in range(N):
		for x in range(M):
			if matrix[h][y][x] == 1:
				q.append([h, y, x])
				time[h][y][x] = 0

while q:
	
	h, y, x = q.popleft()
	nxt = [(h, y - 1, x), (h, y, x + 1), (h, y + 1, x), (h, y, x - 1), (h + 1, y, x), (h - 1, y, x)]

	for nh, ny, nx in nxt:
		if not (0 <= ny < N and 0 <= nx < M and 0 <= nh < H):
			continue
		if time[nh][ny][nx] <= time[h][y][x] + 1:
			continue
		if matrix[nh][ny][nx] == -1:
			continue

		q.append((nh, ny, nx))
		time[nh][ny][nx] = time[h][y][x] + 1

ans = -1
for h in range(H):
	for y in range(N):
		for x in range(M):
			if matrix[h][y][x] != -1:
				ans = max(ans, time[h][y][x])

print(ans if ans != INF else -1)