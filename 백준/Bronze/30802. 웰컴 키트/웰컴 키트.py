N = int(input())
arr = list(map(int, input().split()))
T, P = map(int, input().split())
t = 0

for n in arr:

	if n == 0:
		continue

	if (n // T) == 0:
		t += 1
	elif n // T !=0 and n % T == 0:
		t += n // T
	elif n // T != 0 and n % T != 0:
		t += (n // T) + 1

print(t)
print(N // P, N % P)