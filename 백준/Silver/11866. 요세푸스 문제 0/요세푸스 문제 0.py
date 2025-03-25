from collections import deque

N, K = map(int, input().split())
circle = deque(i for i in range(1, N + 1))
result = []

while circle:
	for i in range(K - 1):
		tmp = circle.popleft()
		circle.append(tmp)

	result.append(circle.popleft())

print('<' +', '.join(map(str, result)) + '>')