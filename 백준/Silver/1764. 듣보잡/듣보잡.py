import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
d = dict()
name_list = []
cnt = 0

for _ in range(N + M):
	name = input()

	if name not in d:
		d[name] = 1
	
	else:
		if d[name] == 1:
			cnt += 1
		d[name] +=1

for name in d.keys():
	if d[name] >= 2:
		name_list.append(name)

name_list = sorted(name_list)
print(cnt)
for name in name_list:
	print(name)