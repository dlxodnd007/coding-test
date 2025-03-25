from collections import deque

T = int(input())

for _ in range(T):
	N, M = map(int, input().split())
	priority = list(map(int, input().split()))
	q = deque()
	cnt = 0

	for i in range(N):
		q.append((i, priority[i]))


	while q:
		cur, pri = q.popleft()

		if any(pri < p for _, p in q):
			q.append((cur, pri))
		else:
			cnt += 1
			if cur == M:
				print(cnt)
				break