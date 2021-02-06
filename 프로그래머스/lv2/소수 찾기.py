from itertools import permutations
def solution(n):
    k = int("".join(sorted(n,reverse = True)))
    d = [True]*(k-1)  
    a = []
    for i in range(2,k//2+1):
        if d[i-2] == True:
            for j in range(i*2,k+1,i):
                d[j-2] = False
    for i in range(1,len(n)+1):
        for j in permutations(n,i):
            if (d[int("".join(j))-2] == True) and int("".join(j)) > 1:
                a.append(int("".join(j)))
    
    return len(set(a))