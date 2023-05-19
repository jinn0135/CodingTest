def solution(n):
    odd = sum([odd_n for odd_n in range(1,n+1) if odd_n%2==1])
    even = sum([even_n**2 for even_n in range(1,n+1) if even_n%2==0])
    return odd if n%2==1 else even