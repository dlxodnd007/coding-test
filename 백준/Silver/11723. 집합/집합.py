import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
S = set()

for _ in range(N):

	q = input()

	if "add" in q :
		S.add(int(q.split()[1]))

	if "remove" in q:
		if int(q.split()[1]) in S:
			S.remove(int(q.split()[1]))

	if "check" in q :
		print(1 if int(q.split()[1]) in S else 0)

	if "toggle" in q:
		if int(q.split()[1]) in S:
			S.remove(int(q.split()[1]))
		else:
			S.add(int(q.split()[1]))

	if "all" in q:
		S = set(range(1, 21))

	if "empty" in q:
		S = set()
