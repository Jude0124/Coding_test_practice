def solution(d, budget):
    d.sort()
    bud = 0
    answer = 0
    for i in d:
        bud += i
        if bud > budget:
            break
        answer+=1
    
    return answer