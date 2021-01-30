def solution(s1, s2):
    S1,S2,I = [],[],[]
    for i in range(len(s1)-1):
        if s1[i:i+2].isalpha() == True:
            S1.append(s1[i:i+2].upper())
            
    for i in range(len(s2)-1):
        if s2[i:i+2].isalpha() == True:
            S2.append(s2[i:i+2].upper())
    
    if S1 + S2 == []:
        return 65536
    
    for i in S2:
        if i in S1:
            S1.remove(i)
            I.append(i)
            
    return int((len(I)/(len(S1)+len(S2))*65536))