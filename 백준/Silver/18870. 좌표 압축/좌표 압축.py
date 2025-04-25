N = int(input())
arr = list(map(int, input().split()))


nums = sorted(set(arr))

convert = dict()
for idx, num in enumerate(nums, 0):
	convert[num] = idx

for i in range(N):
	arr[i] = convert[arr[i]]

print(' '.join(map(str, arr)))