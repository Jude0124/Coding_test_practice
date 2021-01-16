def solution(b,w,t):
    c = (b-1)*[0] +[1]
    cnt =0
    while t !=[]:
        cnt += 1
        c.pop(-1)
        c.insert(0,0)
        if t != []:
            if sum(c)+t[0] <= w:
                c[0] = t.pop(0)
    return cnt+b