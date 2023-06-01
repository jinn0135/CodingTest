def solution(emergency):
    sort_arr = sorted(emergency, reverse=True)
    idx = {num:i+1 for i,num in enumerate(sort_arr)}
    ans = [idx[e] for e in emergency]
    return ans