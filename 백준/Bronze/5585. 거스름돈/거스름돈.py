money = 1000 - int(input())
ans = int(1e12)

for c500 in range(2):
	for c100 in range(10):
		for c50 in range(20):
			for c10 in range(100):
				for c5 in range(200):
					value = (500 * c500) + (100 * c100) + (50 * c50) + (10 * c10) + (5 * c5)

					if money - value >= 0:
						ans = min(ans, c500 + c100 + c50 + c10 + c5 + (money - value))

print(ans)