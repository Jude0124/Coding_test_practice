from itertools import combinations
def solution(n):
    cnt = 0
    r = (1000+999+998)*[True]
    for i in range(2,len(r)//2+1):
        if r[i-1] == True:
            for j in range(i*2,len(r),i):
                r[j-1] = False      
                
    for i in combinations(n,3):
        if r[sum(list(i))-1] == True:
            cnt += 1
    return cnt