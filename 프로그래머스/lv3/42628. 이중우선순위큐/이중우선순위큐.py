from heapq import heapify, heappush, heappop, nlargest
def solution(operations):
    ans = []
    for op in operations:
        if op[0] == 'I': heappush(ans, int(op[2:]))
        elif len(ans)>0:
            if op == 'D 1': ans.remove(nlargest(1, ans)[0])
            elif op == 'D -1': heappop(ans)
    if len(ans)==0: return [0,0]
    return [nlargest(1,ans)[0], ans[0]]