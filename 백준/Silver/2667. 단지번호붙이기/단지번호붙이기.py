from collections import deque

def bfs(y, x):
	global N, matrix, visited, ans

	q = deque()
	cnt = 1
	q.append([y, x])
	visited[y][x] = True

	while q:
		y, x = q.popleft()

		for i in range(4):
			ny = y + dy[i]
			nx = x + dx[i]

			if 0 <= ny < N and 0 <= nx < N and matrix[ny][nx] == 1 and not visited[ny][nx]:
				q.append([ny, nx])
				visited[ny][nx] = True
				cnt += 1

	ans.append(cnt)

N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]
visited = [[False] * (N) for _ in range(N)]
ans = []

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for y in range(N):
	for x in range(N):
		if matrix[y][x] != 0 and not visited[y][x]:
			bfs(y, x)

print(len(ans))  
ans.sort()       
for count in ans:
    print(count)