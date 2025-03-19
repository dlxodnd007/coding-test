N = int(input())
students = [list(map(int, input().split())) for _ in range(N)]
rank_arr = []

for i in range(N):

	rank = 1
	x, y = students[i][0], students[i][1]

	for j in range(N):
		
		if x < students[j][0] and y < students[j][1]:
			rank += 1
			

	rank_arr.append(rank)

for ra in rank_arr:
	print(ra, end = ' ')