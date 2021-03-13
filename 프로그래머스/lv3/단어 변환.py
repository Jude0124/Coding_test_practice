def solution(b, t, w):
    k,b = len(b),[[b]]
    while b:
        tmp = []
        for i in w:
            for m in b:
                if i not in m:
                    cnt = 0
                    for j in range(k):
                        if m[-1][j] != i[j]:
                            cnt += 1
                    if cnt == 1:
                        tmp.append(m+[i])
                        if i == t: return len(m)
        b = tmp[:]
    return 0