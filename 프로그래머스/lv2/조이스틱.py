def solution(n):
    c = 0
    n = list(n)
    for i in range(len(n)):
        c += 13-abs((ord("N")-ord(n[i])))
        
    for i in range(len(n)): 
        if {'A'} in [set(n[i+1:]),set(n[1:len(n) - i])]:
            return c+i
        for j in range(1,(i+1)//2):
            if {'A'} in [set(n[1+j:len(n)-(i-j*2)]),set(n[1+i-j*2:len(n)-j])]:
                return c+i
            
    return c+len(n)-1

# 두번이상 방향을 꺾는 것은 반드시 비효율적이다.
# 단방향(L,R) 양방향(LR,RL) 네가지 경우에 대하여 최단거리부터 loop를 돌며 경로를 탐색한다.