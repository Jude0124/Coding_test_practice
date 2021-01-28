def solution(n, w):
    a = [w[0][0]]
    for i in w:
        if (i not in a) and a[-1][-1] == i[0]:
            a.append(i)
        else:
            return((len(a)-1)%n+1,(len(a)-1)//n+1)
    return [0,0]