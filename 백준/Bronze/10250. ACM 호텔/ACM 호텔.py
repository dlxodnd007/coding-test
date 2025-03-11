n = int(input())

for _ in range(n):
	H, W, N = map(int, input().split())
	f = N % H
	c = N // H + 1

	if f == 0:
		f = H
		c -= 1

	print(str(f) , end = '')
	print(format(c, '02'))