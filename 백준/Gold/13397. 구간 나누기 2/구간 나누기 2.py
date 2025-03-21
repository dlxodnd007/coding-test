import sys
input = lambda: sys.stdin.readline().rstrip()

def is_possible(k):
	global N, M, arr

	cur_mn = arr[0]
	cur_mx = arr[0]
	cnt = 0

	for i in range(1, N):
		cur_mn = min(cur_mn, arr[i])
		cur_mx = max(cur_mx, arr[i])

		if cur_mx - cur_mn > k:
			cur_mn = arr[i]
			cur_mx = arr[i]
			cnt += 1
	cnt += 1

	return (cnt <= M)

N, M = map(int, input().split())
arr = list(map(int, input().split()))

cur = -1
step = 10001

while step != 0:
	while cur + step <= 10000 and not is_possible(cur + step):
		cur += step
	step //= 2

print(cur + 1)