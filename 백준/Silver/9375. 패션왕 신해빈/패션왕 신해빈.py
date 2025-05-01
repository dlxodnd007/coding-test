T = int(input())

for _ in range(T):
    n = int(input())
    fashion = dict()

    for _ in range(n):
        name, category = input().split()
        if category not in fashion:
            fashion[category] = []
        fashion[category].append(name)

    ans = 1
    for category in fashion:
        ans *= (len(fashion[category]) + 1)

    print(ans - 1)