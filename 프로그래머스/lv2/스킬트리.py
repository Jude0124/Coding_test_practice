def solution(s, t):
    s = list(reversed(list(s)))
    cnt = 0
    for i in t:
        pre = 30
        for j in s:
            if j in i and i.find(j)<pre :
                pre = i.find(j)
            elif pre == 30 and j not in i:
                continue
            else:
                cnt +=1
                break
    return len(t)-cnt