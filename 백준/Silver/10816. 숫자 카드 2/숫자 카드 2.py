from collections import Counter

N = int(input())
nums = list(map(int, input().split()))
counter = Counter(nums)

M = int(input())
finds = list(map(int, input().split()))

for find in finds:
	print(counter[find], end = ' ')