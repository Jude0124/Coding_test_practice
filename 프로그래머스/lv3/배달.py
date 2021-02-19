import heapq
from collections import defaultdict
def solution(n,r,k):
    dic = defaultdict(dict)
    s = [0,[1]]
    for i in r:                              # 두 좌표에 대하여 2개 이상의 경로가 존재할 수 있으므로,
        dic[i[0]][i[1]] = 1e4                # 초기값을 최댓값으로 설정한뒤 최소비용 경로로 갱신해줌.
        dic[i[1]][i[0]] = 1e4
    for i in r:
        dic[i[0]][i[1]] = min(dic[i[0]][i[1]],i[2])     
        dic[i[1]][i[0]] = min(dic[i[1]][i[0]],i[2])
    return delivery(dic,s,k)

def delivery(dic,s,k):
    queue,key = [],defaultdict(int)
    heapq.heappush(queue,s)
    while queue:
        p,w = heapq.heappop(queue)
        if (w[-1] not in key) or key[w[-1]] > p:                 # a좌표에서 b좌표로 가는 경로가 무수히 많을 경우
            key[w[-1]] = p                                       # if 문을 통해 신규 경로가 기존의 최소 비용보다 적을 경우만
            for i in dic[w[-1]]:                                 # for문으로 들어가게끔 해주어 불필요한 연산 방지 
                if (i not in w) and dic[w[-1]][i] + p < k+1:  
                    heapq.heappush(queue,[dic[w[-1]][i]+p,w+[i]])        
    return len(key)