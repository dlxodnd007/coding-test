import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
meney = deque()
cnt = 0

for _ in range(N):
	meney.append(int(input()))

while meney:

	tmp = meney.pop()
	cnt += (K // tmp)
	K %= tmp

print(cnt)