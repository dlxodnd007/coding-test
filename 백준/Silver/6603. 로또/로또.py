from itertools import combinations

while True:
	I = list(map(int, input().split()))

	k = I[0]
	arr = I[1:]

	if k == 0:
		break

	for comb in combinations(arr, 6):
		for u in comb:
			print(u , end =' ')
		print()

	print()
