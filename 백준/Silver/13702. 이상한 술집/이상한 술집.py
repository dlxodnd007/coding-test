def is_possible(n):
	global N, K, kettle

	cnt = 0

	for k in kettle:
		cnt += (k // n)

	return cnt >= K

N, K = map(int, input().split())
kettle = [int(input()) for _ in range(N)]

cur = 0
step = max(kettle) + 1

while step != 0:
	while cur + step <= max(kettle) and is_possible(cur + step):
		cur += step
	step //= 2

print(cur)