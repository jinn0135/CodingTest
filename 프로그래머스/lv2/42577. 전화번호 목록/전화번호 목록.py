def solution(phone_book):
    if len(phone_book) == 1: return True
    pb = sorted(phone_book)
    for i in range(len(pb)-1):
        if pb[i]==pb[i+1][:len(pb[i])]: return False
    return True