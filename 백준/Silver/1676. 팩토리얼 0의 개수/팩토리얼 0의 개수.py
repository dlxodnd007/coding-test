def func(x):

	if x == 0:
		return 1

	if x == 1:
		return 1

	return x * func(x - 1)

N = int(input())

f = list(str(func(N)))[::-1]

ans = 0

for s in f:
	if s == '0':
		ans += 1
	else:
		break

print(ans)