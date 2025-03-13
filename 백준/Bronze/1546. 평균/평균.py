N = int(input())
grade = list(map(int, input().split()))

m = max(grade)
sum_grade = 0
for g in grade:
	sum_grade += (g / m) * 100

print(sum_grade / len(grade))