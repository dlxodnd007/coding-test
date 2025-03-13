N = input()
arr = []
sum = 0
for n in range(int(N) -1, 1, -1):
	num = list(str(n))
	
	for i in num:
		sum += int(i)

	if n + sum == int(N):
		arr.append(n)

	sum = 0

if len(arr) == 0:
	print(0)
else:
	print(min(arr))