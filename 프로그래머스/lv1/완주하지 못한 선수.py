def solution(par,com):
    par.sort()
    com.sort()

    for p, c in zip(par, com) :
        if p != c :
            return p  

    return par[-1] 

