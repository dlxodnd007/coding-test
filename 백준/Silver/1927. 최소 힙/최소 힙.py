import heapq
import sys	
input = lambda : sys.stdin.readline().rstrip()

heap = []
N = int(input())

for _ in range(N):

	x = int(input())
	
	if x == 0:
		if heap:
			print(heapq.heappop(heap))
		else:
			print(0)

	else:
		heapq.heappush(heap, x)