import heapq
from collections import defaultdict
def solution(n,r,k):
    dic = defaultdict(dict)
    s = [0,[1]]
    for i in r:           
        dic[i[0]][i[1]] = 1e4+1
        dic[i[1]][i[0]] = 1e4+1
    for i in r:
        dic[i[0]][i[1]] = min(dic[i[0]][i[1]],i[2])
        dic[i[1]][i[0]] = min(dic[i[1]][i[0]],i[2])
    return delivery(dic,s,k)

def delivery(dic,s,k):
    queue,key = [],defaultdict(int)
    heapq.heappush(queue,s)
    while queue:
        p,w = heapq.heappop(queue)
        if (w[-1] not in key) or key[w[-1]] > p:
            key[w[-1]] = p
            for i in dic[w[-1]]:
                if (i not in w) and dic[w[-1]][i] + p < k+1:
                    heapq.heappush(queue,[dic[w[-1]][i]+p,w+[i]])        
    return len(key)