def solution(balls, share):
    return facto(balls)/(facto(balls-share) * facto(share))

def facto(n):
    if n==0 or n==1:
        return 1
    return n*facto(n-1)