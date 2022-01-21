def solution(grid):     # 굳이 알고리즘 분류를 해본다면 다익스트라?? bfs dfs로 풀 수 있지않을까...
    road, answer,cnt = set(),[],0  # road = set 안에 순서대로 앞 두칸은 출발좌표 뒷두칸은 도착좌표를 5번째 칸은 해당 벡터의 방향값을 넣어준다. cnt = 경로의 길이 계산 
    maxX = len(grid)  
    maxY = len(grid[0])

    for i in range(len(grid)):                 # 하나의 격자에서 퍼져나가는 4방향 벡터를 생성
        for j in range(len(grid[0])):
            road.add((i,j,(i-1)%maxX,j,"U"))
            road.add((i,j,(i+1)%maxX,j,"D"))
            road.add((i,j,i,(j-1)%maxY,"L"))
            road.add((i,j,i,(j+1)%maxY,"R"))

    
    while road != set():        #  각각의 격자에 대하여 cycle 함수를 호출하여 벡터의 도착점에서 다음 벡터를 받고 해당 모든 경로들에 대하여 지나갈 set에서 pop 수행
        now = road.pop()
        cnt += 1

        while cycle(grid,now,maxX,maxY) in road:
            cnt += 1
            now = cycle(grid,now,maxX,maxY)
            road.remove(now)
        answer += [cnt]
        cnt = 0
    return sorted(answer)     # 정답은 오름차순으로 정렬하여 제출

def cycle(grid,pos,maxx,maxy):  
    dicR = {"R":"D","D" : "L", "L": "U", "U" : "R"}  # 격자가 R 인 경우에 들어온 방향값을 key으로 나가는 방향을 value로 설정
    dicL = {"R":"U","U" : "L", "L": "D", "D" : "R"}  # 격자가 L 인 경우도 동일하게 딕셔너리 생성
    if grid[pos[2]][pos[3]] == "S": # 직진일 경우 방향값 그대로 유지
        W = pos[4]
    elif grid[pos[2]][pos[3]] == "R": # 우회전일 경우 방향값 딕셔너리에 따라 산출
        W = dicR[pos[4]] 
    else:                             # 좌회전일 경우 방향값 딕셔너리에 따라 산출
        W = dicL[pos[4]]
        
    if W == "U":                            # 각각의 좌표에 대하여 초기화된 방향값을 기준으로 다음 좌표를 들어온 매개변수의 도착점을 출발점으로 계산하여 다음 벡터 산출
        return (pos[2],pos[3],(pos[2]-1)%maxx,pos[3],W)
    elif W == "D":
        return (pos[2],pos[3],(pos[2]+1)%maxx,pos[3],W)
    elif W == "L":
        return (pos[2],pos[3],pos[2],(pos[3]-1)%maxy,W)
    else:
        return (pos[2],pos[3],pos[2],(pos[3]+1)%maxy,W)