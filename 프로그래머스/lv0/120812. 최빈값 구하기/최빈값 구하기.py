from collections import Counter
def solution(array):
    count_arr = Counter(array)
    max_v = max(count_arr.values())
    i = 0
    for k,v in count_arr.items():
        if v==max_v:
            i+=1
            max_k = k
    return max_k if i==1 else -1