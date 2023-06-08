from collections import Counter
def solution(s1, s2):
    return len([k for k,v in Counter(s1+s2).items() if v==2])