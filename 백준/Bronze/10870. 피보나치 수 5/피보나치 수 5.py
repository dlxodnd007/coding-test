N = int(input())

def func(x):
    
    if x == 0:
        return 0
    if x == 1:
        return 1

    return func(x - 1) + func(x - 2)

print(func(N))