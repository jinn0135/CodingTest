from collections import deque
def solution(n, vertex):
    layer = {i:0 for i in range(1,n+1)}
    graph = {i:[] for i in range(1,n+1)}
    for a,b in vertex:
        graph[a].append(b)
        graph[b].append(a)
    visit = deque([1])
    while visit:
        now = visit.popleft()
        for node in graph[now]:
            visit.append(node)
            if layer[node]==0:
                layer[node] = layer[now]+1
            else: 
                layer[node] = min(layer[now]+1, layer[node])
            graph[node].remove(now)
        graph[now] = []
    max_layer = max(layer.values())
    ans = 0
    for k,v in layer.items():
        if v==max_layer:
            ans+=1
    return ans