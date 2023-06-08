def solution(my_string, num1, num2):
    ans = [s for s in my_string]
    temp = ans[num1]
    ans[num1] = ans[num2]
    ans[num2] = temp
    return ''.join(ans)