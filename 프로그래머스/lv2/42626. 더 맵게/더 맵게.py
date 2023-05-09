from heapq import heapify, heappush, heappop
def solution(scoville, K):
    heapify(scoville)
    count = 0
    while scoville[0]<K:
        food1 = heappop(scoville)
        food2 = heappop(scoville)
        heappush(scoville, food1 + 2*food2)
        count += 1
        if len(scoville)==1:
            if scoville[0]<K: return -1
            else: break
    return count