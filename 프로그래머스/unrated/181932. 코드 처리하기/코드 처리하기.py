def solution(code):
    mode, ret = 0, ''
    for i in range(len(code)):
        if code[i]!='1':
            if mode==0 and i%2==0:
                ret += code[i]
            elif mode==1 and i%2==1:
                ret += code[i]
        else:
            mode = 1 if mode==0 else 0
    return ret if ret!='' else 'EMPTY'