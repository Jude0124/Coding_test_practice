def solution(p,s):
    c = []
    pre = 0
    cnt = 1
    for i in range(len(p)):
        now = 0
        now = (100-p[i])//s[i]
        if (100-p[i])%s[i] != 0:
            now+=1
        if pre == 0:
            pre = now  
        elif pre < now:
            c.append(cnt)
            cnt = 1
            pre = now
        else:
            cnt +=1
    c.append(cnt)
    return c




