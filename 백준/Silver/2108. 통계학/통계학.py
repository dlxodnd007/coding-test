from collections import Counter
import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
nums = [int(input()) for _ in range(N)]
counter = Counter(nums).most_common()

# 산술평균
avg = round(sum(nums) / N)
print(avg)

# 중앙값
sorted_nums = sorted(nums)
md = sorted_nums[N // 2]
print(md)

# 최빈값 (여러 개면 두 번째로 작은 값)
max_cnt = counter[0][1]
max_list = [num for num, cnt in counter if cnt == max_cnt]
if len(max_list) == 1:
    print(max_list[0])
else:
    print(sorted(max_list)[1])

# 범위
print(sorted_nums[-1] - sorted_nums[0])
