n = int(input())
arr = list(map(int, input().split()))
cnt = 0
tot = 0

for n in arr:

	cnt = 0

	for i in range(1, n + 1):
		if n % i == 0:
			cnt += 1

	if cnt == 2:
		tot += 1

print(tot)