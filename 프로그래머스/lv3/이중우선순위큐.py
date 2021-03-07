import heapq
def solution(o):
    q = []
    for i in o:
        if i[0] == "I":
            heapq.heappush(q,int(i[2:]))
        elif i[0] == "D" and q != []:
            if i[2] == "1":
                q.pop()
            else:
                heapq.heappop(q)
    if q == []: return [0,0]
    return [max(q),min(q)]