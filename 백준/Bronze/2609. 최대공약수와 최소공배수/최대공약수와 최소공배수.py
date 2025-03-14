N, M = map(int, input().split())

cd = 1
cm = 1

while True:

	flag = False

	for i in range(2, max(N, M) + 1):
		if  N % i == 0 and M % i ==0:
			cd *= i

			N = int(N / i)
			M = int(M / i)
			flag = True
			break

	if flag == False:
		break

print(cd)
print(cd * N * M)