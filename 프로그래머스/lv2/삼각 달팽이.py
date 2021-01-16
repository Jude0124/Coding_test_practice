def solution(n):
    answer =[]
    tray = []
    for i in range(n):
        tray.append([])
        
    cnt = 0
    entry =[]
    for j in [i for i in range(n,0,-1)]:
        tmp =[]
        for k in range(j):
            cnt += 1
            tmp.append(cnt)
        entry.append(tmp)
        
    cnt = 0
    for c in entry:
        if cnt%3 == 0:
            cnt +=1
            for k,v in enumerate(c):
                tray[k+2*(cnt//3)].insert(len(tray[k+2*(cnt//3)])//2,v)
        elif cnt%3 == 1:
            cnt +=1
            tray[n-(cnt//3)-1][1+(cnt//3):1+(cnt//3)] = c
        else:
            cnt +=1
            for k,v in enumerate(c):
                tray[n-k-(cnt//3)-1].insert((len(tray[n-k-(cnt//3)-1])//2)+1,v)
    for i in tray:
        answer.extend(i)

    return answer