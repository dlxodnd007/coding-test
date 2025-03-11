sentence = input().strip().split(' ')
cnt = 0

for s in sentence:
	if s == '':
		continue
	else:
		cnt +=1

print(cnt)