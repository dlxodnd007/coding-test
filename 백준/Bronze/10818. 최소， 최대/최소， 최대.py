n = int(input())
nums = list(map(int, input().split()))
nums.sort()
print(nums[0], nums[len(nums) - 1])