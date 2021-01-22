def solution(s):
    
    while s != "":
        tmp =[]
        for i in s:      
            tmp.append(i)
            if len(tmp)>1:
                if tmp[-1] == tmp[-2]:
                    tmp.pop()
                    tmp.pop()
        if len(s) == len(tmp):
            return 0
        s = "".join(tmp)
    return 1