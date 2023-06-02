def solution(n):
    if n==1: return 1
    ans, check = 0, 2
    for i in range(1,n+1):
        if check==i: break
        elif n%i==0 and i*i==n:
            ans += 1
            break
        elif n%i==0 and check>=i:
            ans += 2
            check = n//i
    return ans