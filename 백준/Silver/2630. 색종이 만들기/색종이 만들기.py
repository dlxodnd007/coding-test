import sys
input = lambda : sys.stdin.readline().rstrip()

def count_paper(y, x, n):
	global white, blue

	color = paper[y][x] # 기준색

	for i in range(y, y + n):
		for j in range(x, x + n):

			if paper[i][j] != color:

				half = n // 2
				count_paper(y, x, half) # 왼쪽 위
				count_paper(y + half, x, half) # 오른쪽 위
				count_paper(y, x + half, half) # 왼쪽 아래
				count_paper(y + half, x + half, half) # 오른쪽 아래
				return

	if color == 0:
		white += 1
	else:
		blue += 1


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0

# 전체 종이에 대해 재귀 시작
count_paper(0, 0, N)

# 결과 출력
print(white)
print(blue)