def solution(num, k):
    if str(k) in str(num):
        return len(str(num).split(str(k))[0])+1
    else: return -1