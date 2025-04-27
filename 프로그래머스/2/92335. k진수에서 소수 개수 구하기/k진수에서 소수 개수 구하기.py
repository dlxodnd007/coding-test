def convert(num, k):
    ret = ""
    
    while num != 0:
        ret = str(num % k) + ret
        num //= k
        
    return ret

def is_prime(num):
    if num == 1:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
    return True
    
    

def solution(n, k):
    num_string = convert(n, k)
    nums = num_string.split('0')
    
    ans = 0
    for num in nums:
        if num != '':
            ans += is_prime(int(num))
        
    return ans
    