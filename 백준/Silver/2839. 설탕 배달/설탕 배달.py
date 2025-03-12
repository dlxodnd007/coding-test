N = int(input())

dp = [5000 for _ in range(5001)]

dp[3] = 1
dp[5] = 1

for i in range(6, N + 1):

	dp[i] = 1 + min(dp[i - 3], dp[i - 5])

if dp[N] >= 5000:
	print(-1)
else:
	print(dp[N])
