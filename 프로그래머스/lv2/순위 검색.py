import itertools
def solution(inf,que):
    answer = []
    dic = {}
    que = [(",".join(que[k].split(" ")[0:7:2]), que[k].split(" ")[-1]) for k in range(len(que))] 
    inf = [inf[m].split(" ") for m in range(len(inf))]
    
    for i in inf:      # 사전 생성 단계에서 모두("-")인 경우를 하나의 case로 판단 4*3*3*3(108) 개의 dic 생성해주기
        i_raw = i[:-1] # 사전보다 query가 길 수 있기 때문에 좀 복잡하더라도 모든 사전을 구축하는 것이 효율적!
        i_raw = i[:-1]
        s = int(i[-1])    
        
        for j in range(5):           
            a = itertools.combinations(range(4),j)            
            for c in a:
                i_dif = i_raw.copy()                
                for o in c:
                    i_dif[o] = '-'                    
                i_all = ','.join(i_dif)
                
                if i_all in dic:
                    dic[i_all].append(s)
                else:
                    dic[i_all] = [s]
                
    for i in dic.values():
        i = i.sort()

    for q in que:
        if q[0] in dic:  
            low = 0
            high = len(dic[q[0]])-1
            while low <= high:
                mid = (high+low)//2
                
                if int(q[1]) <= dic[q[0]][mid]:
                    high = mid-1
                else:
                    low = mid+1
            answer.append(len(dic[q[0]])-low)
        else:
            answer.append(0)
            
    return answer