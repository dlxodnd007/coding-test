def is_possible(k):
	global N, M, heights

	num = 0
	for h in heights:
		if h > k:
			num += (h - k)

	return (num >= M)

N, M = map(int, input().split())
heights = list(map(int, input().split()))

ans = -1

left = -1
right = int(1e9)

while left <= right:
	mid = (left + right) // 2

	if is_possible(mid):
		left = mid + 1
		ans = mid
	else:
		right = mid - 1

print(ans) 