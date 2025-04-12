def is_exist(left):
	global N, M, psum

	cur = left - 1
	step = N

	while step != 0:
		while(cur + step <= N) and (get_sum(left, cur + step) <= M):
			cur += step
		step //= 2

	return (get_sum(left, cur) == M)

def get_sum(a , b):
	global psum
	return psum[b] - psum[a - 1]


N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))
psum = [0] * (N + 1)
ans = 0

for i in range(1, N + 1):
	psum[i] = psum[i - 1] + arr[i]

for left in range(1, N + 1):
	ans += is_exist(left)

print(ans)