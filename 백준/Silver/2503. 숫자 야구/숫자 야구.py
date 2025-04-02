def is_possible(cur):
	global N, infos, check, numbers, choose, ans

	ok = True

	for num , st, bl in infos:
		num = str(num)
		cur_st = cur_bl = 0

		for i in range(3):
			if str(cur[i]) == num[i]:
				cur_st += 1

			elif str(cur[i]) in num:
				cur_bl += 1

		if cur_st != st or cur_bl != bl:
			ok = False
			break

	if ok:
		ans +=1

	return



def permutation(lev):
	global N, infos, check, numbers, choose, ans

	if lev == 3:
		is_possible(choose)
		return

	for i in range(0, len(numbers)):
		if check[i] == True:
			continue

		choose.append(numbers[i])
		check[i] = True

		permutation(lev + 1)

		check[i] = False
		choose.pop()
		

N = int(input())
infos = [list(map(int, input().split())) for _ in range(N)]
check = [False] * (9)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
choose = []
ans = 0

permutation(0)

print(ans)