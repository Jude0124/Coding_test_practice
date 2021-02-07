def solution(c):
    for k,v in enumerate(sorted(c,reverse = True)):
        if k >= v: return k
    return k+1