def solution(rsp):
    rsp_win = {'0':'5','2':'0','5':'2'}
    ans = ''
    for s in rsp:
        ans += rsp_win[s]
    return ans