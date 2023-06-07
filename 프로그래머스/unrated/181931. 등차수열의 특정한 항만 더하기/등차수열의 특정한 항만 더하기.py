def solution(a, d, included):
    ans = 0
    for i in range(1,len(included)+1):
        if included[i-1]:
            ans += a + d*(i-1)
    return ans