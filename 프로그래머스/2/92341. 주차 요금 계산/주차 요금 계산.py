from math import ceil

def convert(string): # '시간:분'을 분 데이터로 고쳐서 반환
    h, m = map(int, string.split(':'))
    return 60 * h + m

def get_fee(use_time, basic_time, basic_fee, unit_time, unit_fee): # use_time에 대한 요금을 계산하여 반환
    if use_time <= basic_time:
        return basic_fee
    
    total_fee = basic_fee
    use_time -= basic_time
    total_fee += ceil(use_time / unit_time) * unit_fee
    
    return total_fee

def solution(fees, records):
    total_time = [0] * 10000 # total_time[i]: i번 차가 주차한 시간
    info = [-1] * 10000 # info[i]: i번 차의 주차한 시각 (-1이면 주차하지 않은 상태를 의미)
    
    # 차량별로 주차한 시간 계산
    for record in records:
        time, num, _ = record.split()
        time = convert(time)
        num = int(num)
        
        if info[num] != -1: # OUT
            total_time[num] += time - info[num]
            info[num] = -1
        else: # IN
            info[num] = time
        
    for num in range(10000):
        if info[num] != -1:
            total_time[num] += (23 * 60 + 59) - info[num]
            info[num] = -1

    return [get_fee(total_time[num], *fees) for num in range(10000) if total_time[num] != 0]
    