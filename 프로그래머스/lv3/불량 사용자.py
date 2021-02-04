import re
from itertools import product
def solution(u, b):
    tmp =[]
    c =0
    for i in range(len(b)):
        b[i] = re.sub("\*","[a-z0-9]",b[i])+"$"
        tmp2 =[]
        for j in u:
            if re.match(b[i],j) != None:
                tmp2.append(re.match(b[i],j).group())
        
        tmp.append(tmp2)
        
    t = []
    for i in list(product(*tmp)):
        if len(i) != len(set(i)):
            continue
        else:
            if sorted(i) not in t:
                t.append(sorted(i))
                c += 1
    return c