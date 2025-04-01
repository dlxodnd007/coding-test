def comp(x):

	return (x[1] * x[2] * x[3], x[1] + x[2] + x[3], x[0])


N = int(input())

students = [list(map(int, input().split())) for _ in range(N)]

students = sorted(students, key = comp)

for b, p, q, r in students[:3]:
	print(b, end = ' ')