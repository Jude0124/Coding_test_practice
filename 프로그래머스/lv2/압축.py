def solution(m):
    dic = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    ans = []
    while 1:
        for i in range(len(m),0,-1):
            if m[0:i] in dic:
                ans.append(dic.index(m[0:i])+1)
                w = m[0:i]
                m = m[i:]
                break
        if len(m) != 0:
            dic.append(w+m[0])
        else:
            break

    return ans