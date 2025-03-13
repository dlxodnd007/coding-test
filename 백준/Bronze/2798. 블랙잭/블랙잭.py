from itertools import combinations
n, m = map(int, input().split())
cards = list(map(int, input().split()))
ans = 0

for comb in combinations(cards, 3):
    s = sum(comb)
    if s <= m and s > ans:
        ans = s

print(ans)