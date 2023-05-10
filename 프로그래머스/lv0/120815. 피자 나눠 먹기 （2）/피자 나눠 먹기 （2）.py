def solution(n):
    bcd_nm = bcd(n,6) # 최대공약수
    lcd_nm = bcd_nm * (n/bcd_nm) * (6/bcd_nm) # 최대공배수
    return lcd_nm//6 

def bcd(n,m=6): 
    if n%m==0:
        return m
    return bcd(m,n%m)