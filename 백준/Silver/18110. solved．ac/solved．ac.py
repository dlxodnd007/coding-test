import sys
input = lambda : sys.stdin.readline().rstrip()

def roundUp(n):
	if ( n - int(n)) >= 0.5:
		return int(n) + 1
	else:
		return int(n)

N = int(input())

if N == 0:
	print(0)
	sys.exit()

top_15 = roundUp(N * 0.15) 
bot_15 = roundUp(N * 0.15)

solved = sorted(list(int(input()) for _ in range(N)))
solved = solved[top_15 : len(solved) - bot_15]
grade = roundUp(sum(solved) / len(solved))

print(grade)