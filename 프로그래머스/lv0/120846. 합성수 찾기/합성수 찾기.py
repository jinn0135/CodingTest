def solution(n):
    if n==1: return 0
    ans = 0
    for i in range(2,n+1):
        if not prime_n(i):
            ans += 1
    return ans

def prime_n(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True