def fact(x):

	if x == 0:
		return 1

	return fact(x - 1) * x

def permutation(lev):
	global S, ans, choose, check

	if lev == len(S):
		ok = True
		for i in range(0, len(choose) - 1):
			if choose[i] == choose[i + 1]:
				ok = False
				break
		ans += ok
		return

	for i in range(0, len(S)):
		if check[i] == True:
			continue

		choose.append(S[i])
		check[i] = True

		permutation(lev + 1)

		choose.pop()
		check[i] = False



S = input()
ans = 0
choose = []
check = [False] * (len(S))

permutation(0)

for i in range(ord('a'), ord('z') + 1):
	ans //= fact(S.count(chr(i)))

print(ans)