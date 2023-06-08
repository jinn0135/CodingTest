def solution(my_string):
    my_s = my_string.split()
    ans = int(my_s[0])
    for i in range(1,len(my_s),2):
        if my_s[i]=='+':
            ans += int(my_s[i+1])
        elif my_s[i]=='-':
            ans -= int(my_s[i+1])
    return ans