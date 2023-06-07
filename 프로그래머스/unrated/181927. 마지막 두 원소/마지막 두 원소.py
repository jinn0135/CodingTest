def solution(numli):
    return numli+[numli[-1]-numli[-2]] if numli[-1]>numli[-2] else numli+[numli[-1]*2]