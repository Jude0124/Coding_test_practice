def solution(p):
    def s(p):
        a,c,d = "",0,True
        if p == "": return p
        for i in range(len(p)):
            if p[i] == "(": c += 1
            else: c -= 1
            if c < 0: d = False
            if c == 0:
                u = p[:i+1]
                v = p[i+1:]
                break
        if d == True:
            a += u + s(v)
            return a
        else:
            a += "("+ s(v) +")"
            for i in range(1,len(u)-1):
                if u[i] == ")":
                    a += "("
                else: a += ")"
            return a
    return s(p)