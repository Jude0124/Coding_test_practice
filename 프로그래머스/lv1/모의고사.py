def solution(answers):
    ans1 =[1,2,3,4,5]
    ans2 =[2,1,2,3,2,4,2,5]
    ans3 =[3,3,1,1,2,2,4,4,5,5]
    cnt1=cnt2=cnt3=0
    for i in range(len(answers)):
        if ans1[i%5] == answers[i]:
            cnt1 +=1
        if ans2[i%8] == answers[i]:
            cnt2 +=1
        if ans3[i%10] == answers[i]:
            cnt3 +=1
    cnt = [cnt1,cnt2,cnt3]
    return [i+1 for i,value in enumerate(cnt) if value == max(cnt)]

