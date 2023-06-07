def solution(s):
    s = s.split()
    ans, i = 0, 0
    while i<len(s):
        if i!=len(s)-1 and s[i+1]=='Z':
            i += 2
        else:
            ans += int(s[i])
            i += 1
    return ans