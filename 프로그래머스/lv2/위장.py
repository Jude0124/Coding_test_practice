def solution(c):
    return eval("*".join([str([k[1] for k in c].count(i)+1) for i in set([i[1] for i in c])]))-1