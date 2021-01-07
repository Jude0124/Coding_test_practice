def solution(n, lost, reserve):
    ans = set()
    new_reserve = set(reserve)-set(lost) 
    new_lost = set(lost)-set(reserve) 
    cnt = 0
    for i in new_reserve: 
        if i-1 in new_lost: 
            cnt+=1

        elif i+1 in new_lost: 
            cnt+=1
            new_lost.remove(i+1)


        
        return n-len(new_lost)+cnt