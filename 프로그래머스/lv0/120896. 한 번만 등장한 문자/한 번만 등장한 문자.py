from collections import Counter
def solution(s):
    count = Counter(s)
    ans = [k for k in count.keys() if count[k]==1]
    return ''.join(sorted(ans))