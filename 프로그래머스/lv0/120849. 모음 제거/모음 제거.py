def solution(my_string):
    for vol in ['a','e','i','o','u']:
        my_string = my_string.replace(vol,'')
    return my_string