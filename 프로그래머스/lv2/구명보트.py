def solution(p, l):
    c,s,e = 0,0,len(p)-1
    p = sorted(p,reverse = True)
    while s <= e:
        if p[s]*2 <= l:
            c += (e+2-s)//2
            break
        if p[s]+p[e] <= l:
            s += 1
            e -= 1
            c += 1
        else:
            s += 1
            c += 1
    return c