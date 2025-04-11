import sys
input = lambda : sys.stdin.readline().rstrip()

def get_sum(a, b):
	global psum, arr
	return psum[b] - psum[a - 1]


N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))
psum = [0] * (N + 1)

for i in range(1 , N + 1):
	psum[i] = psum[i - 1] + arr[i]

for _ in range(M):
	a, b = map(int, input().split())
	print(get_sum(a, b))