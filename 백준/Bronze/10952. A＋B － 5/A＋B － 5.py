import sys

while True:
    line = sys.stdin.readline().rstrip()
    
    if not line:
        break
        
    A , B = map(int, line.split())
    if A == 0 and B == 0:
        break
        
    print(A + B)
    
     