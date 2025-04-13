def is_possible(n):
	global N, arr, M

	ans = 0

	for i in range(N):
		if arr[i] <= n:
			ans += arr[i]
		else:
			ans += n

	return ans <= M

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

cur = 0
step = max(arr) + 1

while step != 0:
	while cur + step <= max(arr) and is_possible(cur + step):
		cur += step
	step //= 2

print(cur)