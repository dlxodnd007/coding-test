import sys


while True:
	line = sys.stdin.readline().rstrip()

	if not line or line == '0':
		break

	pr = list(line)
	isTrue = True

	for i in range(0, len(pr) // 2 + 1):

		if pr[i] != pr[len(pr) - 1 - i]:
			isTrue = False
			break
	
	if isTrue:
		print('yes')
	else:
		print('no')