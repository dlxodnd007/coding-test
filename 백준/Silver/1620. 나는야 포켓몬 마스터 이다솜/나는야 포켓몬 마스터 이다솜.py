import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
name_to_num_poketmones = dict()
num_to_name_poketmones = dict()

for i in range(1, N + 1):
	poketmon = input()
	name_to_num_poketmones[poketmon] = i
	num_to_name_poketmones[i] = poketmon

for _ in range(M):

	q = input()

	if q.isdigit():
		print(num_to_name_poketmones[int(q)])
	else:
		print(name_to_num_poketmones[q])
		