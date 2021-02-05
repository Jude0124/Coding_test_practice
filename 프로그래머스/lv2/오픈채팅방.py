def solution(r):
    d,a = {},[]
    for i in r:
        t = i.split(" ")
        if t[0] == "Leave": a.append([t[1],"님이 나갔습니다."])
        else:
            d[t[1]] = t[2]
            if t[0] == "Enter": a.append([t[1],"님이 들어왔습니다."])
    for j in range(len(a)): a[j] = d[a[j][0]] + a[j][1]        
    return a