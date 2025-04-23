N = int(input())
P = list(map(int, input().split()))
cnt = []
tmp = 0
P = sorted(P)

for p in P:
	tmp += p
	cnt.append(tmp)

print(sum(cnt))