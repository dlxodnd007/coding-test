import sys
input = lambda: sys.stdin.readline().rstrip()

def solution(N, graph):
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if graph[j][i] == 1 and graph[i][k] == 1:
                    graph[j][k] = 1
    return graph

# input
N = int(input())
graph = list(list(map(int,input().split())) for _ in range(N))

# result
result = solution(N, graph)
for res in result:
    print(*res)