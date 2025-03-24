def is_possible(k):
	global N, K, cables

	cnt = 0

	# print(k)

	for cable in cables:
		cnt += cable // k

	return cnt >= N

K, N = map(int, input().split())
cables = [int(input()) for _ in range(K)]

cur = 0
step = max(cables) + 1

while step != 0:
	while cur + step <= max(cables) and is_possible(cur + step):
		cur += step
	step //= 2

print(cur)