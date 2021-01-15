def solution(p, l):
    cnt = 0
    x =  [i for i in range(len(p))]
    while l in x:
        while p[0] != max(p):
            p.append(p.pop(0))
            x.append(x.pop(0))
        p.pop(0)
        x.pop(0)
        cnt += 1    
    return cnt