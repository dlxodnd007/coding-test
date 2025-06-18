import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
M = int(input())
S = input()

left , right = 0, 0
cnt = 0

while right < M:
	if S[right : right + 3] == 'IOI':
		right += 2

		if right - left == 2 * N:
			cnt += 1
			left += 2

	else:
		right += 1
		left = right

print(cnt)