import sys
input = lambda : sys.stdin.readline().rstrip()

T = int(input())

dp = [0] * (1001)

dp[0] = 1

for _ in range(T):
	n = int(input())

	for i in range(1, n + 1):
		dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

	print(dp[n])