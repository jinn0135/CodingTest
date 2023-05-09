import numpy as np
def solution(n, results):
    if n==1 or n==2: return n
    graph = [[np.nan for i in range(n)] for i in range(n)]
    for i in range(len(graph)):
        graph[i][i] = 0
    for a,b in results:
        graph[a-1][b-1] = 1 # win
        graph[b-1][a-1] = -1 # lose
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if graph[i][k]==1 and graph[k][j]==1:
                    graph[i][j] = 1
                    graph[j][i] = -1
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if graph[i][k]==1 and graph[k][j]==1:
                    graph[i][j] = 1
                    graph[j][i] = -1                
    
    ans = 0
    for i in range(n):
        if np.isnan(graph[i]).sum()==0:
            ans += 1
    print(graph)
    return ans