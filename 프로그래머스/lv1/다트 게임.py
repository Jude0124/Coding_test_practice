def solution(dartResult):
    score1 = "" 
    score2 = []
    cnt =0
    for i in list(dartResult):
        if i.isdigit():
            score1+=i
        else:
            score1+=" "
            score2.append(i)
    score1 = score1.split()   

    for j in score2:
        if j.isalpha():
            cnt+=1
            if cnt == 1:
                if j == "S":
                    score1[0] = int(score1[0])
                elif j == "D":
                    score1[0] = int(score1[0])**2
                else: 
                    score1[0] = int(score1[0])**3
            if cnt == 2:
                if j == "S":
                    score1[1] = int(score1[1])
                elif j == "D":
                    score1[1] = int(score1[1])**2
                else: 
                    score1[1] = int(score1[1])**3
            if cnt == 3:
                if j == "S":
                    score1[2] = int(score1[2])
                elif j == "D":
                    score1[2] = int(score1[2])**2
                else: 
                    score1[2] = int(score1[2])**3

        else: 
            if cnt == 1:
                if j == "*":
                    score1[0] *=2
                else:
                    score1[0] *=-1
            if cnt == 2:
                if j == "*":
                    score1[0] *=2
                    score1[1] *=2
                else:
                    score1[1] *=-1
            if cnt == 3:
                if j == "*":
                    score1[1] *=2
                    score1[2] *=2
                else:
                    score1[2] *=-1
                    
    return sum(score1)
