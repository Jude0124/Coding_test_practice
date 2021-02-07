def solution(n,t):
    n = [[-n[0],n[0]]]+n[1:]
    def target(l,t):
        if len(l) == 1: return l[0].count(t)
        b,a = [],l.pop()
        for i in l[0]:
            b.append(i+a)
            b.append(i-a)
        l[0] = b
        return target(n,t)
    return target(n,t)