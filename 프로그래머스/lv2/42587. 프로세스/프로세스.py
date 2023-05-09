from collections import deque
def solution(priorities, location):
    pri_que = deque(priorities)
    loca_que = deque([0 for i in range(len(priorities))])
    loca_que[location] = 1
    
    while len(loca_que)!=0 and max(loca_que)==1:
        if pri_que[0]==max(pri_que):
            pri_que.popleft()
            loca_que.popleft()
        else:
            pri_que.append(pri_que.popleft())
            loca_que.append(loca_que.popleft())
    return len(priorities)-len(loca_que)