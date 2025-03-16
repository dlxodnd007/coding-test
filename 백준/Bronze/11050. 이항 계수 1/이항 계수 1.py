from itertools import combinations
N, K = map(int, input().split())
ans = 0
for comb in combinations(range(1, N + 1), K):
	ans += 1

print(ans)