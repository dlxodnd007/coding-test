N = int(input())
step = [0] + list(int(input()) for _ in range(N))
dp = [0] * (N + 1)

if N >= 1:
    dp[1] = step[1]
if N >= 2:
    dp[2] = step[1] + step[2]

for i in range(3, N + 1):
	dp[i] = max(dp[i - 2], dp[i - 3] + step[i - 1]) + step[i]

print(dp[N])