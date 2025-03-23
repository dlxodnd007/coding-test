import sys
from collections import deque

while True:

	line = sys.stdin.readline().rstrip()

	if line == '.':
		break

	st = list(line)

	d = deque()
	balanced = True

	for s in st:

		if s == '(' or s == '[':
			d.append(s)

		elif s == ')':
			if len(d) == 0:
				balanced = False
				break
			elif d[-1] != '(':
				balanced = False
				break
			else:
				d.pop()

		elif s == ']':
			if len(d) == 0:
				balanced = False
				break
			elif d[-1] != '[':
				balanced = False
				break
			else:
				d.pop()

	print('yes' if balanced and len(d) == 0 else 'no')
