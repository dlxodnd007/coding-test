N = int(input())
cnt = 0
result = 0

for i in range(N):
	arr = list(input())
	result = 0
	for ch in arr:
		if ch == 'O':
			cnt += 1
			result += cnt
		else:
			cnt = 0
	cnt = 0
	print(result)
