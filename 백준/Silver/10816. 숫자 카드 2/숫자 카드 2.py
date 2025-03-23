N = int(input())
nums = list(map(int, input().split()))
num_dict = {}

for num in nums:
	if num in num_dict:
		num_dict[num] += 1
	else:
		num_dict[num] = 1

M = int(input())
finds = list(map(int, input().split()))

for find in finds:
	print(num_dict.get(find, 0) , end = ' ')
