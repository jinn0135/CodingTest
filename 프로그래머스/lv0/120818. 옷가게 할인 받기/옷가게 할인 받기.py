def solution(price):
    if price>=500000: sale = 0.8
    elif price>=300000: sale = 0.9
    elif price>=100000: sale = 0.95
    else: sale = 1
    return int(price*sale)