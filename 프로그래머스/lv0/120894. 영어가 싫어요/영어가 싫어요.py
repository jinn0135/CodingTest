def solution(numbers):
    e2n = {'on':['one','1'],'tw':['two','2'],'th':['three','3'],
           'fo':['four','4'],'fi':['five','5'],'si':['six','6'],
           'se':['seven','7'],'ei':['eight','8'],'ni':['nine','9'],
           'ze':['zero','0']}
    ans = ''
    while numbers:
        ans += e2n[numbers[:2]][1]
        numbers = numbers[len(e2n[numbers[:2]][0]):]
    return int(ans)