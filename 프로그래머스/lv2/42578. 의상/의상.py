def solution(clothes):
    cloth_dic = {k:[] for _,k in clothes}
    for v, k in clothes:
        cloth_dic[k].append(v)
    check = 1
    for v in cloth_dic.values():
        check *= (len(v)+1)
    return check-1