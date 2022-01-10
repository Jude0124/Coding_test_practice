def solution(places):
    for i in range(5): # Index error 방지를 위한 가벽 설치
        places[i] = ["XXXXX"] + places[i] + ["XXXXX","XXXXX"]
        for j in range(8): places[i][j] = "X" + places[i][j] + "XX"
    answer = []
    for room in places:
        state = 1
        for i in range(1,6):
            for j in range(1,6):
                if room[i][j] == "P":
                    if room[i][j+1] == "P" or room[i+1][j] == "P":
                        state = 0
                    elif (room[i+1][j+1] == "P") and ("O" in [room[i][j+1] , room[i+1][j]]):
                        state = 0
                    elif room[i+2][j]+room[i+1][j] == "PO":
                        state = 0       
                    elif room[i][j+2]+room[i][j+1] == "PO":
                        state = 0
                    elif room[i-1][j+1] == "P" and ("O" in [room[i][j+1], room[i-1],[j]]):
                        state = 0
                    elif room[i+1][j-1] == "P" and ("O" in [room[i][j-1], room[i+1],[j]]):
                        state = 0 
                                                    
        answer.append(state)
    return answer