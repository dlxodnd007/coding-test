import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
nums = [int(input()) for _ in range(n)]

nums = sorted(nums)

for n in nums:
	print(n)