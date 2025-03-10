N = int(input())

for _ in range(N):

	R, S = input().split()
	r = int(R)
	s = list(S)

	for i in s:
		print(i * r, end = '')

	print()