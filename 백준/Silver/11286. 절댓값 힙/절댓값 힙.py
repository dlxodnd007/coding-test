import sys, heapq
input = lambda : sys.stdin.readline().rstrip()

n = int(input())

q = []
for i in range(n):
	num = int(input())

	if num == 0:
		if q: 
			print(heapq.heappop(q)[1])
		else:
			print(0)

	else:
		heapq.heappush(q,(abs(num), num))