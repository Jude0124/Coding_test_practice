from collections import deque
def solution(b):
    N = len(b)
    board = [[1]*(N+2) for _ in range(N+2)]
    for i in range(1,N+1):
        for j in range(1,N+1):
            board[i][j] = b[i-1][j-1]
            
    s = ((1,1),(1,2),0)                             # 초기 위치
    queue = deque([s])
    verif = set([((1,1),(1,2))])
    while queue:
        now = queue.popleft()
        if now[0] == (N,N) or now[1] == (N,N):      # 최종위치 도달시 출력, 경주로 건설 문제와 다른점 == (단위시간에 따른 비용이
            return now[2]                           # 독립사건들에 대하여 모두 같기 때문에, 최초 도달 track == 최소 비용 track)
        for i in move(now,board):
            if (i[0],i[1]) not in verif:            # 한번 거쳐간 좌표 재방문 방지
                verif.add((i[0],i[1]))              
                queue.append(i)

def move(q,b):
    cur1,cur2 = q[0],q[1]
    tmp = []
    p = [(0,1),(0,-1),(1,0),(-1,0)]
    for x,y in p:                               # 평행이동
        next1 = (cur1[0]+x,cur1[1]+y)
        next2 = (cur2[0]+x,cur2[1]+y)
        if (b[next1[0]][next1[1]] == 0) and (b[next2[0]][next2[1]] == 0):
            tmp.append((next1,next2,q[2]+1))
    
    if cur1[0] == cur2[0]:                      # 모빌이 수평인경우 회전
        for x in [1,-1]:
            if b[cur1[0]+x][cur1[1]] == 0 and b[cur2[0]+x][cur2[1]] == 0:
                next1 = (cur1[0]+x,cur1[1])
                next2 = (cur1[0]+x,cur2[1])
                tmp.append((next1,cur1,q[2]+1))
                tmp.append((next2,cur2,q[2]+1))
    else:                                      # 모빌이 수직인경우 회전
        for x in [1,-1]:
            if b[cur1[0]][cur1[1]+x]  == 0 and b[cur2[0]][cur2[1]+x] == 0:
                next1 = (cur1[0],cur1[1]+x)
                next2 = (cur2[0],cur2[1]+x)
                tmp.append((cur1,next1,q[2]+1))
                tmp.append((cur2,next2,q[2]+1))       
    return tmp