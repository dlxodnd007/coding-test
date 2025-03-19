def is_exist(arr, num):
	left = 0
	right = len(arr) - 1

	while left <= right:
		mid = (left + right) // 2

		if arr[mid] < num:
			left = mid + 1

		if arr[mid] > num:
			right = mid - 1

		if arr[mid] == num:
			return 1

	else:
		return 0 



N = int(input())
arr = sorted(list(map(int, input().split())))

M = int(input())
nums = list(map(int, input().split()))

for num in nums:
	print(is_exist(arr, num))