vows = ['a', 'e', 'i', 'o', 'u']

def is_possible():
	global L, C, arr, choose

	vow = 0
	for u in choose:
		vow += u in vows

	con = L - vow

	return con >= 2 and vow >= 1

def combination(idx, lev):
	global L, C, arr, choose

	if lev == L:
		if is_possible():
			print(''.join(choose))
		return

	for i in range(idx, C):
		choose.append(arr[i])
		combination(i + 1, lev + 1)
		choose.pop()

L, C = map(int, input().split())
arr = list(input().split())
choose = []

arr.sort()

combination(0, 0)