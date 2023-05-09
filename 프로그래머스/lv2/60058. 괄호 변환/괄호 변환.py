from collections import deque
def solution(p):
    if p=='': return p

    a_n, b_n = 0, 0
    for i in range(len(p)):
        if p[i]=='(': a_n += 1
        elif p[i]==')': b_n += 1
        if a_n!=0 and a_n==b_n:
            u, v = p[:i+1], p[i+1:]
            break
    if right_p(u): return u+solution(v)
    
    ans = '('+solution(v)+')'
    for s in u[1:-1]:
        if s=='(': ans += ')'
        elif s==')': ans += '('
    return ans

def right_p(p):
    if p=='': return True
    p, stack = deque(p), deque([])
    while p:
        s = p.popleft()
        if s=='(': stack.append(s)
        elif s==')':
            if len(stack)==0:
                return False
            stack.pop()
    if len(p)==0: return True
    else: return False