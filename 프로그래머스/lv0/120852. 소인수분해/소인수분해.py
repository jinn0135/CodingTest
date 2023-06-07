def solution(n):
    if prime_n(n): return [n]
    ans, num = [], n
    for i in range(2,n//2+1):
        if prime_n(i):
            while num%i==0:
                num = num//i
                ans.append(i)
        if num==1: break
    return sorted(list(set(ans)))

def prime_n(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return False
    return True