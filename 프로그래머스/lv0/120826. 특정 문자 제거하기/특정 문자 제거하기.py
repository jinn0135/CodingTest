def solution(my_string, letter):
    ans = ''
    for s in my_string:
        if s==letter:
            continue
        ans += s
    return ans