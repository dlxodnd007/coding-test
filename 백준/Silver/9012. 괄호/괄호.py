from collections import deque

N = int(input())

for _ in range(N):
	ps = list(input())
	q = deque()
	for p in ps:
		if p == '(':
			q.append(p)
		elif p == ')':
			if len(q) == 0:
				q.append(p)
				break
			else:
				q.pop()
	
	print('YES' if len(q) == 0 else 'NO')