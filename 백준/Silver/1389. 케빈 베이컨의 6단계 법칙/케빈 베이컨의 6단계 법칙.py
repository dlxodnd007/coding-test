from collections import deque

def bfs(n):
	global graph, friends

	q = deque()
	q.append(n)

	while q:
		cnt = q.popleft()

		for num in friends[cnt]:
			if num == n:
				continue
			if graph[n][num] == 0:
				graph[n][num] = graph[n][cnt]+1
				q.append(num)

	return sum(graph[n])

n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
friends = [[] for _ in range(n + 1)]

for _ in range(m):
	a, b = map(int, input().split())
	friends[a].append(b)
	friends[b].append(a)

temp = 500000
answer = 0
for i in range(1, n + 1):
	if temp > bfs(i):
		temp = bfs(i)
		answer = i
print(answer)