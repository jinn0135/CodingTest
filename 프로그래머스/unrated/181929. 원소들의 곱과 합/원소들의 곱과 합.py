def solution(num_list):
    sum_n = sum(num_list)
    prod_n = 1
    for n in num_list:
        prod_n *= n
    return 1 if prod_n<sum_n**2 else 0