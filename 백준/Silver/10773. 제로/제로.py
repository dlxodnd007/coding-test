import sys
from collections import deque

N = int(input())
d = deque()

for _ in range(N):

	n = int(input())

	if n != 0:
		d.append(n)
	else:
		if len(d) == 0:
			continue
		else:
			d.pop()


print(sum(d))