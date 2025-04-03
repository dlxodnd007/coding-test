def combination(idx):
	global N, S, arr, ans, choose

	if idx == N:
		if sum(choose) == S and len(choose) >= 1:
			ans +=1
		return

	choose.append(arr[idx])
	combination(idx + 1)
	choose.pop()

	combination(idx + 1)

N, S = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
choose = []

combination(0)

print(ans)