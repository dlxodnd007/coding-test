from math import sqrt

M, N = map(int, input().split())

result = 0
is_prime = [True for _ in range(N + 1)]

is_prime[1] = False

for i in range(2, int(sqrt(N)) + 1):
    if is_prime[i]:
        for j in range(2 * i, N + 1, i):
            is_prime[j] = False

for i in range(M, N + 1):
	if is_prime[i]:
		print(i)