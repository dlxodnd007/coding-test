import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
fruits = list(map(int, input().split()))
start = 0
answer = 0
d = defaultdict(int) 

for end in range(n):
    d[fruits[end]] += 1

    while len(d) > 2: 
        d[fruits[start]] -= 1 
        if d[fruits[start]] == 0:
            del d[fruits[start]]
        start += 1

    answer = max(answer, end - start + 1)

print(answer)