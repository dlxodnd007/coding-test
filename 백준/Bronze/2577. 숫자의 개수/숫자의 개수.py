import sys

dt = dict()
mul = 1
cnt = 0

while True:
	line = sys.stdin.readline().strip()
	if not line:
		break
	mul *= int(line)

num = list(str(mul))
for n in num:
	if n in dt:
		dt[n] += 1
	else:
		dt[n] = 1

for i in range(10):
	if str(i) in dt:
		print(dt[str(i)])
	else:
		print(0)