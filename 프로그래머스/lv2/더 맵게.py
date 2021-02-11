import heapq
def solution(s, K):
    heapq.heapify(s)
    c = 0
    while s[0] < K:
        if len(s) == 1:
            return -1
        c += 1
        heapq.heappush(s,heapq.heappop(s)+heapq.heappop(s)*2)
    return c