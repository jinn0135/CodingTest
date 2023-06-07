def solution(my_string):
    count, ans = {s:0 for s in my_string}, ''
    for s in my_string:
        if count[s]==0:
            ans += s
            count[s] = 1
    return ans