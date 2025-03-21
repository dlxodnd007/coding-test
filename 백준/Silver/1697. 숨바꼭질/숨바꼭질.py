from collections import deque

MAX = int(1e5)

N, K = map(int, input().split())

q = deque()
visited = [False] * (MAX + 1)

q.append([0, N])
visited[N] = True

while q:
	time, pos = q.popleft()

	if pos == K:
		print(time)
		exit()

	for nxt_pos in [pos - 1, pos + 1, pos * 2]:
		if (0 <= nxt_pos <= MAX) and (not visited[nxt_pos]):
			q.append([time + 1, nxt_pos])
			visited[nxt_pos] = True
