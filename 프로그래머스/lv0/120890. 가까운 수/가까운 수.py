def solution(array, n):
    dic = {a:abs(a-n) for a in sorted(array)}
    ans, min_abs = 0, 100
    for k,v in dic.items():
        if v<min_abs:
            ans = k
            min_abs = v
    return ans