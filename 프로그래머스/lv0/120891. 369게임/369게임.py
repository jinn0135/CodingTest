from collections import Counter
def solution(order):
    count = Counter(str(order))
    return count['3'] + count['6'] + count['9']