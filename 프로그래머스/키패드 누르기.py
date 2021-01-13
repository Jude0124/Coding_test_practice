def get_distance(A,B):
    dist = { 1 : (-1,1) , 2 : (0,1) , 3 : (1,1),
             4 : (-1,0) , 5 : (0,0) , 6 : (1,0),
             7 : (-1,-1), 8 : (0,-1), 9 : (1,-1),
             10 : (-1,-2), 0 : (0,-2), 12 : (1,-2)}
    x,y = dist[A]
    x2,y2 = dist[B]
    return abs(x2-x)+abs(y2-y)

def solution(numbers,hand):
    answer = ""
    ind_L = 10
    ind_R = 12
    for i in numbers:
        if i in [1,4,7]:
            answer+="L"
            ind_L = i
        elif i in [3,6,9]:
            answer+="R"
            ind_R = i
        else:
            if get_distance(ind_L,i) == get_distance(ind_R,i):
                answer+=hand[0].upper()
                if hand == "right":
                    ind_R = i
                else:
                    ind_L = i
            elif get_distance(ind_L,i) > get_distance(ind_R,i):
                answer+="R"
                ind_R = i
            else:
                answer+="L"
                ind_L = i

    return answer