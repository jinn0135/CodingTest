def solution(my_string):
    ans = []
    for s in my_string:
        try: ans.append(int(s))
        except: continue
    return sorted(ans)