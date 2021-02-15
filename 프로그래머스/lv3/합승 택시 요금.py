import heapq
from collections import defaultdict

def solution(n,s,a,b,f):
    dic = defaultdict(dict)  
    for i in f:
        dic[i[0]][i[1]] = i[2]
        dic[i[1]][i[0]] = i[2]
    
    best = 2e9
    for k,v in bestfee(dic,s).items():      
        best = min(best,bestfee(dic,k)[a]+bestfee(dic,k)[b]+ v)

    return best

def bestfee(dic,s):
    fee = {i : 2e7 for i in dic}
    fee[s], queue = 0, []
    heapq.heappush(queue,[fee[s],s])
    
    while queue:
        acc,spot= heapq.heappop(queue)
        for i in dic[spot]:
            tmp = dic[spot][i]+acc
            if tmp < fee[i]:
                heapq.heappush(queue,[tmp,i])
                fee[i] = tmp
    return fee


# 최적경로 문제 , 다익스트라
# 딕셔너리로 모든 경로 등록 후(dic), 출발점으로부터 모든 지점에 대하여 최소비용 딕셔너리로 반환(fee)
# 출발점을 포함한 모든 지점에 대하여 최소비용 계산(합승지점)
# 모든 지점에 대하여 목적지(a,b)를 향한 최소비용 계산
# 세 비용을 합한 값이 최솟값이 될때마다 최적비용 갱신