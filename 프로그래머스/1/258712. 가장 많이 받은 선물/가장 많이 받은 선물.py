def solution(friends, gifts):
    N = len(friends)
    I = {name: idx for name, idx in zip(friends, range(N))}
    
    record = [[0] * N for _ in range(N)]
    give = [0] * N
    receive = [0] * N
    
    for g in gifts:
        a, b = g.split()
        give[I[a]] += 1
        receive[I[b]] += 1
        record[I[a]][I[b]] += 1

    score = [0] * N
    for x in range(N):
        score[x] = give[x] - receive[x]
        
    gifts = [0] * N
    for x in range(N):
        for i in range(N):
            if x == i: continue
            case1 = (record[x][i] > record[i][x])
            case2 = (record[x][i] == record[i][x] and score[x] > score[i])
            gifts[x] += (case1 or case2)

    return max(gifts)