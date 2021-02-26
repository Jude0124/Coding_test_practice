from collections import defaultdict
def solution(n,c):
    tray = [i for i in range(n)]
    cnt = 0
    dic = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if (i != j) and c[i][j] == 1:
                dic[i].append(j)
    while tray:             
        k = tray.pop()
        search,tmp = [k],[k]
        while search:      
            nxt = []
            for i in search:
                for j in dic[i]:
                    if j not in tmp:
                        tmp.append(j)
                        nxt.append(j)
            search = nxt
        tray = list(set(tray)-set(tmp))
        cnt += 1
        
    return cnt