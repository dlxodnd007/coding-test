N = int(input())
arr = []
for i in range(1, N + 1):
	age, name = input().split()
	arr.append((age, name, i))

arr = sorted(arr, key = lambda x : (int(x[0]), x[2]))

for a in arr:
	print(a[0], a[1])