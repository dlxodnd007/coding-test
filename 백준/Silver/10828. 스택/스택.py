import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

N = int(input())
st = deque()

for i in range(N):

	s = input()

	if 'push' in s:
		x = int(s.split()[1])
		st.append(x)	

	elif s == 'pop':
		print(st.pop() if st else -1)

	elif s == 'size':
		print(len(st))

	elif s == 'empty':
		print(1 if not st else 0)

	elif s == 'top':
		print(st[-1] if st else -1)