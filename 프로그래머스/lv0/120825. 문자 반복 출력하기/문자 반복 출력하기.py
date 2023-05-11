def solution(my_string, n):
    ans = ''
    for s in [s*n for s in my_string]:
        ans+=s
    return ans