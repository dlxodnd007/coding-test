N = int(input())
arr = list(input())
H = 0
MOD = 1234567891
for i in range(N):
	H += (ord(arr[i]) - 96) * pow(31,i)

print(H % MOD)