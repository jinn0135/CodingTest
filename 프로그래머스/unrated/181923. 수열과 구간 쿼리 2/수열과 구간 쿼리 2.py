def solution(arr, queries):
    ans = []
    for s,e,k in queries:
        temp = [a for a in arr[s:e]+[arr[e]] if a>k]
        if temp==[]: ans.append(-1)
        else: ans.append(min(temp))
    return ans