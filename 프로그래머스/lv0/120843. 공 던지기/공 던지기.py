def solution(numbers, k):
    l = len(numbers)
    odd_ns, even_ns, i = [], [], 1
    while 2*i<=l+1:
        odd_ns.append(2*i-1)
        even_ns.append(2*i)
        i+=1
        
    if l%2==0: new_ns = odd_ns
    else: new_ns = odd_ns + even_ns[:-1]
    
    if k%len(new_ns)==0: return new_ns[-1]
    else: return new_ns[k%len(new_ns)-1]