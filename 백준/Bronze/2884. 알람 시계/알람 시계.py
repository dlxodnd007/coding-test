H, M = map(int, input().split())

if H >=0 and M >= 45:
	print(H, (M-45))

elif H > 0 and M < 45:
	print((H -1),(60 - (45 - M)))

elif H == 0 and M < 45:
	print((24 -1),(60 - (45 - M)))