import heapq
def solution(maps): # 다익스트라 문제
    c,d = len(maps),len(maps[0])
    m = [[0]*(d+2) for _ in range(c+2)]  # 외벽 만들어주기
    for a in range(c):
        for b in range(d):
            m[a+1][b+1] = maps[a][b]

    s,delta,deck = [(1,1,1)],[(1,0),(-1,0),(0,1),(0,-1)],{(1,1)} # 기존 이동 경로를 집합자료형으로 deck에 추가, 중복방지

    while s:
        cnt,x,y = heapq.heappop(s)
        if (x,y) == (c,d):
            return cnt
        for w,z in delta:
            if (x+w,y+z) not in deck and m[x+w][y+z] == 1:
                deck.add((x+w,y+z))
                heapq.heappush(s,(cnt+1,x+w,y+z))
    return -1
