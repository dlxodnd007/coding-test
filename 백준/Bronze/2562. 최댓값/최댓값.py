# BOJ 2562
import sys
nums = dict()
cnt = 0
while True:
	line = sys.stdin.readline().strip()

	if not line:
		break

	nums[int(line)] = cnt
	cnt += 1

nums_arr = sorted(nums)
print(nums_arr[len(nums_arr) - 1])
print(nums[nums_arr[len(nums_arr) - 1]] + 1)