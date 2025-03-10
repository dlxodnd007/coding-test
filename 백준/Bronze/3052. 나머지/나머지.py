import sys

s = set()

while True:
    line = sys.stdin.readline().strip() 
    if not line:  
        break
    s.add(int(line) % 42)

print(len(s))