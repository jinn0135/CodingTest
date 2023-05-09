def solution(triangle):
    answer = sumF(triangle)
    return answer[0]

def sumF(triangle):
    if len(triangle) == 1:
        return triangle[0]
    t = sumF(triangle[1:])
    for j in range(len(triangle[0])):
        triangle[0][j] += max(t[j],t[j+1])
    return triangle[0]