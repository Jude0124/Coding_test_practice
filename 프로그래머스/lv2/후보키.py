import itertools
def solution(r):
    
    r = list((list(i) for i in zip(*r)))
    k = sum([list(itertools.combinations([i for i in range(len(r))],i)) for i in range(1,len(r)+1)],[])  
    cnt = 0
    
    while k != []:    
        tmp = []
        for j in k[0]:
            tmp.append(r[j])
        tmp = list(i for i in zip(*tmp))

        if len(tmp) == len(set(tmp)):             
            cnt+=1 
            for i in range(len(k)-1,-1,-1):
                if set(k[0]) - set(k[i]) == set():
                    k.pop(i)
        else:
            k.pop(0)
            
    return cnt