import math

n = int(input())
dp = [1 if math.sqrt(i).is_integer() else 0 for i in range(50001)]
dp[0] = 0

for i in range(2, n + 1):

	if math.sqrt(i).is_integer():
		continue

	bf = math.floor(math.sqrt(i))
	min_value = i

	while bf > 0:
		min_value = min(min_value, 1 + dp[i - bf ** 2])
		bf -= 1

	dp[i] = min_value

print(dp[n])