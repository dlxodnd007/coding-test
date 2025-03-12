import sys

while True:
	line = sys.stdin.readline()

	if not line or line.split()[0] == '0':
		break

	tr = sorted(list(map(int, line.split())))

	if pow(tr[0], 2) + pow(tr[1], 2) == pow(tr[2], 2):
		print("right")
	else:
		print("wrong")