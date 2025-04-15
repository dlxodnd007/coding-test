def rotate(y1, x1, y2, x2):
    global matrix
    
    pos = []
    for x in range(x1, x2 + 1):
        pos.append((y1, x))
    for y in range(y1 + 1, y2 + 1):
        pos.append((y, x2))
    for x in range(x2 - 1, x1 - 1, -1):
        pos.append((y2, x))
    for y in range(y2 - 1, y1, -1):
        pos.append((y, x1))
    N = len(pos)
    
    for i in range(N - 1, 0, -1):
        ny, nx = pos[i][0], pos[i][1]
        by, bx = pos[i - 1][0], pos[i - 1][1]
        matrix[ny][nx], matrix[by][bx] = matrix[by][bx], matrix[ny][nx]
    
    return min(matrix[y][x] for y, x in pos)

def solution(rows, columns, queries):
    global matrix
    
    
    matrix = [[0] * (columns) for _ in range(rows)]
    for y in range(rows):
        for x in range(columns):
            matrix[y][x] = x + y * columns + 1
    
    ans = []
    for y1, x1, y2, x2 in queries:
        ans.append(rotate(y1 - 1, x1 - 1, y2 - 1, x2 - 1))
    
    return ans