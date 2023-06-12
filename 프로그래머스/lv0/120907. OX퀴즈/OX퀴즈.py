def solution(quiz):
    ans = []
    for q in quiz:
        x,s,y,_,z = q.split()
        if s=='+': z2 = int(x)+int(y)
        else: z2 = int(x)-int(y)
        if z2==int(z):
            ans.append('O')
        else: ans.append('X')
    return ans