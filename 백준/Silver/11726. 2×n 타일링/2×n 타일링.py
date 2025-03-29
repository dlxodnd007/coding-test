import sys
sys.setrecursionlimit(int(1e6))

def func(n):
	global dp

	if n == 1 or n == 2:
		return n

	if dp[n] != -1:
		return dp[n]

	dp[n] = (func(n - 1) + func(n - 2)) % 10007

	return dp[n]


N = int(input())

dp = [-1] * (N + 2)

print(func(N))