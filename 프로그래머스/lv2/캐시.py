def solution(s,c):
    t,cnt = [1]*s,0
    if s == 0: return 5*len(c)
    for i in c:
        if i.upper() in t[:s]:
            cnt += 1
            t.remove(i.upper())
        t.insert(0,i.upper())
    return 5*len(c)-4*cnt