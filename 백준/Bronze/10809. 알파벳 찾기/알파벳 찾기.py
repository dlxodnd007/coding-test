arr = list(input())


result = [-1 for _ in range(26)]
cnt = 0
for ch in arr:
	if result[ord(ch) - 97] == -1:
		result[ord(ch) - 97] = cnt
	cnt += 1

print(' '.join(map(str, result)))