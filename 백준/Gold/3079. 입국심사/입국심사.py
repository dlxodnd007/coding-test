import sys
input = lambda : sys.stdin.readline().rstrip()

def is_possible(t):
	global N, M, times
	cnt = 0
	for i in range(N):
		cnt += t // times[i]
	return cnt >= M

N, M = map(int, input().split())
times = [int(input()) for _ in range(N)]

low = 0
high = max(times) * M
ans = high

while low <= high:
	mid = (low + high) // 2
	if is_possible(mid):
		ans = mid
		high = mid - 1
	else:
		low = mid + 1

print(ans)