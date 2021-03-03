def solution(dirs):
    U,D,L,R = (1,0),(-1,0),(0,-1),(0,1)
    x,y,deck,cnt = 0,0,{()},0
    for i in dirs:
        a,b = eval(i)
        if -6<x+a<6 and -6<y+b<6:
            if ((x,y),(x+a,y+b)) not in deck:
                deck.add(((x,y),(x+a,y+b)))
                deck.add(((x+a,y+b),(x,y)))
                cnt += 1
            x,y = x+a,y+b
    return cnt