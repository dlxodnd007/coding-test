s = input().split('-')

sum = 0
for i in s[0].split('+'):
	sum += int(i)

for i in s[1:]:
	for j in i.split('+'):
		sum -= int(j)

print(sum)